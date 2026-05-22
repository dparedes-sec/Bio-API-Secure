from pydantic import BaseModel, field_validator
import re

DNA_PATTERN = re.compile(r'^[ACGTN]+$', re.IGNORECASE)

class SequenceCreate(BaseModel):
    name: str
    sequence: str
    organism: str | None = None

    @field_validator('sequence')
    @classmethod
    def validate_dna_sequence(cls, v: str) -> str:
        if not v:
            raise ValueError('Sequence cannot be empty')
        if len(v) > 1_000_000:
            raise ValueError('Sequence exceeds maximum length of 1,000,000 bp')
        if not DNA_PATTERN.match(v):
            raise ValueError(
                'Invalid DNA sequence: only A, C, G, T, N characters allowed'
            )
        return v.upper()

class SequenceResponse(BaseModel):
    id: int
    name: str
    sequence: str
    organism: str | None
    created_by: int

    model_config = {'from_attributes': True}
