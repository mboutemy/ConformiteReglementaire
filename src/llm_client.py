"""
Client LLM — version mockée
"""

import json
import re
from datetime import date

_VALIDITY_STATUTS = ["valide", "abrogé"]
_STOPWORDS = {"sur", "la", "le", "les", "des", "de", "du", "d'", "et"}
_REGULATIONS = {
    "REG-001": {
        "code": "RGD-2024",
        "full_name": "Règlement sur la Gouvernance des Données 2024",
        "domain": "gouvernance",
        "effective_date": date(2024, 1, 1),
        "revision_date": None,
        "criticality": "HIGH",
    },
    "REG-002": {
        "code": "DSI-2023",
        "full_name": "Directive Sécurité des Systèmes d'Information 2023",
        "domain": "sécurité",
        "effective_date": date(2023, 7, 1),
        "revision_date": None,
        "criticality": "HIGH",
    },
    "REG-003": {
        "code": "PCR-2022",
        "full_name": "Protocole de Continuité et Résilience 2022",
        "domain": "business_continuity",
        "effective_date": date(2022, 1, 1),
        "revision_date": date(2024, 1, 1),
        "criticality": "MEDIUM",
    },
    "REG-008": {
        "code": "DPO-2023",
        "full_name": "Circulaire Délégué Protection des Données 2023",
        "domain": "DPO",
        "effective_date": date(2023, 3, 1),
        "revision_date": None,
        "criticality": "LOW",
    },
    "REG-011": {
        "code": "DPO-2024",
        "full_name": "Extension Circulaire Délégué Protection des Données 2024",
        "domain": "DPO",
        "effective_date": date(2024, 3, 1),
        "revision_date": None,
        "criticality": "LOW",
    },
}

def _check_validity_date(check_date: date, begin_date: date, end_date: date) -> bool:
    """Renvoie True si la date est valide"""
    if end_date is None:
        return check_date >= begin_date
    if end_date <= begin_date:
        return False
    return begin_date <= check_date <= end_date

def _contains_domain_keyword(text: str, keyword: str) -> bool:
    """Renvoie True si le mot keyword correspondant au domaine est présent dans le texte"""
    return re.search(rf"\b{re.escape(keyword.strip())}\b", text, re.IGNORECASE) is not None

def _significant_words(full_name: str) -> list:
    """Mots du nom complet utilisables pour un rapprochement, hors mots StopWords et années"""
    return [
        word for word in full_name.split()
        if word.lower().strip("’'") not in _STOPWORDS and not word.isdigit() and len(word) > 3
    ]

def _needs_review(comment: str) -> str:
    return json.dumps([{"status": "needs_review", "comment": comment}], ensure_ascii=False)

class LLMClient:
    """
    Recherche les réglementations applicables à un message en tenant compte de leur validité temporelle.
    """

    def complete(self, prompt: str) -> str:
        text = prompt.lower()
        today = date.today()

        matched = {}  # contiendra les réglementations trouvées
        for regulation_id, reg in _REGULATIONS.items():
            if _contains_domain_keyword(text, reg["domain"]):
                matched[regulation_id] = reg

        # si un mot du texte n'est pas trouvé dans domain, on vérifie si le full_name de la réglementation est présent
        if not matched:
            for regulation_id, reg in _REGULATIONS.items():
                if any(_contains_domain_keyword(text, word) for word in _significant_words(reg["full_name"])):
                    matched[regulation_id] = reg

        # si aucune réglementation n'est trouvée, on renvoie un message de review
        if not matched:
            return _needs_review("Aucune réglementation correspondante trouvée.")

        work_regulations = []
        # pour la lsite des réglementations matched, on vérifie la validité temporelle
        for regulation_id, reg in matched.items():
            valide = _check_validity_date(today, reg["effective_date"], reg["revision_date"])
            work_regulations.append({
                "regulation_id": regulation_id,
                "code": reg["code"],
                "domain": reg["domain"],
                "criticality": reg["criticality"],
                "validity": _VALIDITY_STATUTS[0] if valide else _VALIDITY_STATUTS[1],
                "status": "ok" if valide else "needs_review",
            })

        domains = {reg["domain"] for reg in work_regulations}
        # si plusieurs domaines sont trouvés, on renvoie un message de review
        if len(domains) > 1:
            return _needs_review("Plusieurs domaines trouvés : " + ", ".join(sorted(domains)))
        # sinon (1 seul domaine trouvé)
        regulations = [reg for reg in work_regulations if reg["validity"] == _VALIDITY_STATUTS[0]]

        if not regulations:
            return _needs_review("Aucune réglementation en vigueur trouvée à la date du jour.")

        return json.dumps(regulations, ensure_ascii=False)
