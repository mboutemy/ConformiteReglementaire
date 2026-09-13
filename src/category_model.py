"""Modèle ML de catégorisation — version mockée
"""
CATEGORIES = ("DPO", "cybersecurity", "business_continuity", "gouvernance")

# Mots-clés par "domain" simplifié
_KEYWORDS = {
    "DPO": ("dpo", "délégué protection", "délégué à la protection", "délégué de protection"),
    "cybersecurity": ("sécurité", "cybersécurité", "pénétration", "incident"),
    "business_continuity": ("continuité", "reprise d'activité", "résilience", "sinistre", "rto"),
    "gouvernance": ("gouvernance", "données", "conservation", "traçabilité", "archivage"),
}


class MLCategoryModel:
    """Classifieur de catégorie, interface façon scikit-learn."""

    def predict(self, messages: list[str]) -> list[str]:
        return [self._predict_one(message) for message in messages]

    def _predict_one(self, message: str) -> str:
        text = message.lower()
        for category, keywords in _KEYWORDS.items():
            if any(keyword in text for keyword in keywords):
                return category
        return "autre"
