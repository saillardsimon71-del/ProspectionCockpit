from __future__ import annotations

from datetime import datetime

from pydantic import Field

from sqlmodel import SQLModel, Field as SQLField

import uuid

from enum import Enum


class ConsentStatus(str, Enum):
    """Statuts possibles pour un consentement."""

    PENDING = "pending"  # Double opt-in en attente
    GRANTED = "granted"
    REVOKED = "revoked"
    EXPIRED = "expired"


class ConsentBase(SQLModel):
    """Base pour Consent."""

    lead_id: uuid.UUID
    channel: str = Field(..., description="email | sms | linkedin | whatsapp")
    granted_at: datetime | None = None
    revoked_at: datetime | None = None
    source: str | None = Field(default=None)  # comment le consentement a été obtenu
    double_opt_in_token: str | None = None


class ConsentCreate(SQLModel):
    """Payload création consentement."""

    lead_id: uuid.UUID
    channel: str
    source: str | None = None


class ConsentRead(ConsentBase):
    """Modèle de lecture."""

    id: uuid.UUID
    status: ConsentStatus


class Consent(ConsentBase, table=True):
    """Entité DB Consent (core pour conformité RGPD)."""

    __tablename__ = "consents"

    id: uuid.UUID = SQLField(default_factory=uuid.uuid4, primary_key=True)
    status: ConsentStatus = SQLField(default=ConsentStatus.PENDING, nullable=False, index=True)
    created_at: datetime = SQLField(default_factory=datetime.utcnow, nullable=False)
