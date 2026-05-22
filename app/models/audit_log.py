from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.sql import func
from app.database import Base

class AuditLog(Base):
    __tablename__ = 'audit_logs'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=True)  # None for unauthenticated
    action = Column(String(100), nullable=False)  # CREATE, READ, UPDATE, DELETE
    resource = Column(String(100), nullable=False)  # sequences, users
    resource_id = Column(Integer, nullable=True)
    ip_address = Column(String(45), nullable=False)
    user_agent = Column(String(255), nullable=True)
    status_code = Column(Integer, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
