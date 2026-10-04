"""Modèle ML de catégorisation — version mockée
"""
from typing import Optional
from pathlib import Path
import json

DOMAIN = ("data_governance", "cybersecurity", "business_continuity", "audit", "cloud", "ai_governance", "data_protection", "incident_management", "data_retention")

DEFAULT_ARTIFACT_PATH = Path(__file__).parent.parent / "models" / "category_model_v1.json"


class MLCategoryModel:
    """Classifieur de domaine, interface façon scikit-learn."""
    def __init__(self, artifact_path: Path = DEFAULT_ARTIFACT_PATH):
        artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
        self.version = artifact["version"]
        self._keywords = artifact["keywords"]

    def predict(self, messages: list[str]) -> list[Optional[str]]:
        """Un domaine par message, ou None si aucun domaine n'est reconnu."""
        return [self._predict_one(message) for message in messages]

    def _predict_one(self, message: str) -> Optional[str]:
        text = message.lower()
        for domain, keywords in self._keywords.items():
            if any(keyword in text for keyword in keywords):
                return domain
        return None
