"""Domain layer - Entities, Value Objects, Domain Services."""

from .lead import Lead, LeadCreate, LeadRead

from .consent import Consent, ConsentCreate, ConsentRead, ConsentStatus

__all__ = [
    "Lead",
    "LeadCreate",
    "LeadRead",
    "Consent",
    "ConsentCreate",
    "ConsentRead",
    "ConsentStatus",
]
