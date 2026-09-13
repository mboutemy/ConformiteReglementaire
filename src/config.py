"""
Lecture de la configuration depuis les variables d'environnement.
"""

import os


def get_llm_api_key() -> str:
    """Clé du provider LLM. Le mock ne l'utilise pas, mais le circuit
    de lecture est en place pour le jour où un vrai provider arrive."""
    return os.getenv("LLM_API_KEY", "")


def get_log_level() -> str:
    return os.getenv("LOG_LEVEL", "INFO")
