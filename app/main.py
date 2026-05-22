from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from app.middleware.headers import SecurityHeadersMiddleware
from app.middleware.audit import AuditLogMiddleware
from app.routers import auth, sequences, users
from app.database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title='Bio API',
    description='Secure REST API for biological sequence data',
    version='1.0.0',
    docs_url='/docs' if True else None,  # Deshabilitar en produccion
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(AuditLogMiddleware)

app.include_router(auth.router, prefix='/auth', tags=['auth'])
app.include_router(sequences.router, prefix='/sequences', tags=['sequences'])
app.include_router(users.router, prefix='/users', tags=['users'])

@app.get('/health')
def health_check():
    return {'status': 'healthy'}
