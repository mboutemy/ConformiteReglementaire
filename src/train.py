"""« Entraînement » du modèle de domaine — version mockée.

Un vrai projet exécuterait ici son pipeline d'entraînement (préparation,
fit, évaluation). Le mock produit le même RÉSULTAT qu'un entraînement :
un ARTEFACT versionné (models/category_model_v1.json) que le reste du
code charge sans savoir comment il a été fabriqué.

C'est le point important : l'entraînement et le serving sont deux
CYCLES DE VIE différents. Ce script tourne parfois (nouvelle réglementation,
nouveau domaine, mots-clés révisés) puis s'arrête ; la classification tourne
à chaque message. Ils ne communiquent que par l'artefact — jamais par un
import direct.

Usage :
    uv run python -m src.train
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

DEFAULT_ARTIFACT_PATH = Path(__file__).parent.parent / "models" / "category_model_v1.json"

# Les « données d'entraînement » du mock : la table de mots-clés par domaine.
# Un vrai entraînement produirait des poids ; le principe est identique :
# le résultat est un FICHIER versionnable, pas du code.
# L'ordre compte : le modèle renvoie le premier domaine dont un mot-clé matche.
_KEYWORDS = {
    "data_governance": ["gouvernance des données", "conservation", "traçabilité", "archivage"],
    "cybersecurity": ["sécurité", "cybersécurité", "chiffrement", "données sensibles", "test de pénétration"],
    "business_continuity": ["continuité", "reprise d'activité", "résilience", "heures", "rto"],
    "audit": ["audit", "traçabilité", "inspection", "vérification"],
    "cloud": ["cloud", "localisation", "région"],
    "ai_governance": ["intelligence artificielle", "machine learning", "scoring", "automatisées", "automatique"],
    "data_protection": ["dpo", "délégué protection", "délégué à la protection", "délégué de protection", "protection des données"],
    "incident_management": ["incident", "gestion des incidents"],
    "data_retention": ["rétention", "conserve", "durée de conservation", "durée de rétention", "archivage", "suppression"],
}


def train(artifact_path: Path = DEFAULT_ARTIFACT_PATH) -> dict:
    artifact = {
        "model": "keywords-domain-model",
        "version": "v1",
        "trained_at": date.today().isoformat(),
        "keywords": _KEYWORDS,
    }
    artifact_path.parent.mkdir(parents=True, exist_ok=True)
    artifact_path.write_text(
        json.dumps(artifact, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Modèle entraîné et sauvegardé : {artifact_path}")
    return artifact


if __name__ == "__main__":
    train()
