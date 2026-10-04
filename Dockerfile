# Image de l'application : suffisante, pas optimisée.
# (multi-stage, cache fin, user non-root : plus tard, si un symptôme le réclame)
FROM python:3.12-slim

# uv : installation des dépendances, rapide et reproductible
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# Les dépendances d'abord : cette couche n'est reconstruite que si
# pyproject.toml ou uv.lock changent. --frozen : exactement le lock,
# rien d'autre — la même installation chez tout le monde.
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-cache
ENV PATH="/app/.venv/bin:$PATH"

COPY src/ src/
COPY prompts/ prompts/
COPY donnees/ donnees/
COPY models/ models/

# Démonstration : classifie un cas connu nominal.
CMD ["python", "-m", "src.cli", "Nous n'avons pas de DPO désigné mais traitons les données de 800 clients."]
