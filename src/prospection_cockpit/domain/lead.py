from __future__ import annotations

from datetime import datetime

from pydantic import EmailStr, Field

from sqlmodel import SQLModel, Field as SQLField

import uuid


class LeadBase(SQLModel):
    """Base model for Lead."""

    email: EmailStr = Field(..., description="Email du lead (unique)")
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str | None = Field(default=None, max_length=100)
    phone: str | None = Field(default=None, max_length=20)
    company: str | None = Field(default=None, max_length=200)
    city: str | None = Field(default=None, max_length=100)
    postal_code: str | None = Field(default=None, max_length=10)
    source: str | None = Field(default=None, description="Source du lead (CSV, import, etc.)")
    notes: str | None = Field(default=None)


class LeadCreate(LeadBase):
    """Payload for creating a new lead."""

    pass


class LeadRead(LeadBase):
    """Read model with system fields."""

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime | None = None
    score: float | None = Field(default=None, ge=0, le=100, description="Score IA 0-100")
    score_reason: str | None = None


class Lead(LeadBase, table=True):
    """Database entity for Lead."""

    __tablename__ = "leads"

    id: uuid.UUID = SQLField(default_factory=uuid.uuid4, primary_key=True, index=True)
    created_at: datetime = SQLField(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime | None = SQLField(default=None)
    score: float | None = SQLField(default=None)
    score_reason: str | None = SQLField(default=None)

    # Future: relationship to consents, interactions, etc.
