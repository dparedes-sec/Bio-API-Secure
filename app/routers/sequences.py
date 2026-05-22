from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from slowapi import Limiter
from slowapi.util import get_remote_address
from app.database import get_db
from app.models.sequence import Sequence
from app.models.user import UserRole
from app.schemas.sequence import SequenceCreate, SequenceResponse
from app.core.security import get_current_user, require_role

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)

@router.get('/', response_model=list[SequenceResponse])
@limiter.limit('100/minute')
def list_sequences(
    request: Request,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if limit > 100:
        raise HTTPException(status_code=400, detail='Limit cannot exceed 100')
    return db.query(Sequence).offset(skip).limit(limit).all()

@router.post('/', response_model=SequenceResponse, status_code=201)
@limiter.limit('100/minute')
def create_sequence(
    request: Request,
    sequence_in: SequenceCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role(UserRole.lab_technician, UserRole.admin))
):
    sequence = Sequence(**sequence_in.model_dump(), created_by=current_user.id)
    db.add(sequence)
    db.commit()
    db.refresh(sequence)
    return sequence

@router.delete('/{sequence_id}', status_code=204)
@limiter.limit('100/minute')
def delete_sequence(
    request: Request,
    sequence_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_role(UserRole.admin))
):
    sequence = db.query(Sequence).filter(Sequence.id == sequence_id).first()
    if not sequence:
        raise HTTPException(status_code=404, detail='Sequence not found')
    db.delete(sequence)
    db.commit()
