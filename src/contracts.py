"""
Contrats d'entrée / sortie du service, en Pydantic.
"""

from typing import Literal, Optional
from pydantic import BaseModel

Domain = Literal["data_governance", "cybersecurity", "business_continuity", "audit", "cloud", "ai_governance", "data_protection", "incident_management", "data_retention"]
Criticality = Literal["HIGH", "MEDIUM", "LOW"]


class MessageInput(BaseModel):
    """Entrée : un message à qualifier dans la cadre de la conformité réglementaire, tel que reçu."""
    message: str


class ClassificationResult(BaseModel):
    """Sortie : le contrat stable des 4 phases.

    En cas de refus (message vide ou hors périmètre), status vaut
    "needs_review" et aucun domaine ni criticité n'est inventée.
    """
    regulation_id: Optional[str]
    code: Optional[str]
    domain: Optional[Domain]
    criticality: Optional[Criticality]
    status: Literal["ok", "needs_review"]
    comment: Optional[str]  # commentaire est utilisé pour expliquer dans le cas où le status "needs_review"
