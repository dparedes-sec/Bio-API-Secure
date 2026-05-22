from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.audit_log import AuditLog
from app.core.security import oauth2_scheme
from jose import jwt, JWTError
from app.core.config import settings

METHOD_TO_ACTION = {
    'GET': 'READ',
    'POST': 'CREATE',
    'PUT': 'UPDATE',
    'PATCH': 'UPDATE',
    'DELETE': 'DELETE',
}

class AuditLogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        # Skip health check and docs endpoints
        if request.url.path in ('/health', '/docs', '/openapi.json'):
            return response

        user_id = None
        auth_header = request.headers.get('Authorization', '')
        if auth_header.startswith('Bearer '):
            try:
                token = auth_header.split(' ')[1]
                payload = jwt.decode(
                    token, settings.secret_key, algorithms=[settings.algorithm]
                )
                user_id = payload.get('sub')
            except JWTError:
                pass

        resource = request.url.path.split('/')[1] if '/' in request.url.path else 'unknown'

        db: Session = SessionLocal()
        try:
            log = AuditLog(
                user_id=user_id,
                action=METHOD_TO_ACTION.get(request.method, request.method),
                resource=resource,
                ip_address=request.client.host,
                user_agent=request.headers.get('User-Agent', '')[:255],
                status_code=response.status_code,
            )
            db.add(log)
            db.commit()
        finally:
            db.close()

        return response
