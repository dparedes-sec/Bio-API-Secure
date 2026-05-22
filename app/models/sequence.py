from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from app.database import Base

class Sequence(Base):
    __tablename__ = 'sequences'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    sequence = Column(Text, nullable=False)
    organism = Column(String(255))
    created_by = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
