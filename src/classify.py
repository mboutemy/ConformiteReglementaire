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

import json

from src.category_model import MLCategoryModel
from src.llm_client import LLMClient

_category_model = MLCategoryModel()
_llm_client = LLMClient()


def _is_out_of_scope(message: str) -> bool:
    """Hors périmètre : message sans aucune lettre (ex. « ??? », « 1234 »)."""
    return not any(char.isalpha() for char in message)


def _build_prompt(message: str) -> str:
    return (
        "Tu aides les auditeurs de l'ACSI. Identifie les réglementations applicables"
        " à l'élément d'audit et vérifie leur validité temporelle "
        "et donne aussi la criticité globale (HIGH, MEDIUM ou LOW). Renvoie une liste de JSON "
        "{\"regulation_id\": ..., \"code\": ..., \"domain\": ..., \"criticality\": ..., \"validity\": ...,  \"status\": ...}"
        f" si des réglementations sont trouvées, sinon {{\"status\": \"needs_review\", \"comment\": ...}} : {message} "

    )


def classify(message: str) -> dict:
    if not message.strip() or _is_out_of_scope(message):
        return [{"status": "needs_review", "comment": "Aucune réglementation correspondante trouvée."}]

    category = _category_model.predict([message])[0]
    raw_response = _llm_client.complete(_build_prompt(message))
    response = json.loads(raw_response)

    return response
