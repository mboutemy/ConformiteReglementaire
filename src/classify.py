"""Orchestration de la classification : ML + LLM + rejet en cas d'ambiguïté.

Si le message est vide ou n'a pas de réglementation correspondante ou correspond à plusieurs domaines, on renvoie un status needs_review.
Sinon, on renvoie une liste de dictionnaires JSON, chacun correspondant à une liste de réglementations trouvées

- regulation_id : id de la réglementation identifiée
- code : code associé à la réglementation identifiée
- domain : domaine associé à la réglementation identifiée
- criticality : criticité associée à la réglementation identifiée
- status      : "ok"
                ou 
                "needs_review" si aucune réglementation ne correspond ou si plusieurs domaines sont trouvés, 
                ou si une réglementation citée est obsolète
"""
from dotenv import load_dotenv
import os
import logging
import json
from pathlib import Path

from src.category_model import MLCategoryModel
from src.llm_client import LLMClient

load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
# Configure logging
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)


_category_model = MLCategoryModel()
_llm_client = LLMClient()

# Recuperation du prompt versionné dans le fichier prompts/classify_v1.txt
_PROMPT_TEMPLATE = (Path(__file__).parent.parent / "prompts" / "classify_v1.txt").read_text(encoding="utf-8")

def _build_prompt(message: str, domain: str) -> str:
    return _PROMPT_TEMPLATE.format(message=message, domain=domain)

def _is_out_of_scope(message: str) -> bool:
    """Hors périmètre : message sans aucune lettre (ex. « ??? », « 1234 »)."""
    return not any(char.isalpha() for char in message)

def _needs_review(comment: str) -> list[dict]:
    return [{"regulation_id": None, "code": None, "domain": None,
             "criticality": None, "status": "needs_review", "comment": comment}]

def classify(message: str) -> dict:
    if not message.strip() or _is_out_of_scope(message):
        return _needs_review("Aucune réglementation correspondante trouvée.")

    domain = _category_model.predict([message])[0]
    print("domain:", domain)
    if domain is None:
        return _needs_review("Aucun domaine réglementaire reconnu.")

    raw_response = _llm_client.complete(_build_prompt(message, domain))
    response = json.loads(raw_response)

    return response
