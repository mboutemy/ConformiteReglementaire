# Conformité Réglementaire | AuditPro MVP — Préparation de dossier d'audit

## Phase 1 : Make it work
[Contenu de la phase 1](PHASE1.md)

## Installation et lancement

```
uv sync
source .venv/bin/activate
cp .env.example .env

python3 -m src.cli "Nous n'avons pas de DPO désigné mais traitons les données de 800 clients"
```

## Phase 2 : Make it explicit
[Contenu de la phase 2](PHASE2.md)

## **Installation et lancement.**

### Récupérer le projet :
```
git checkout phase2_code

uv sync
source .venv/bin/activate
cp .env.example .env
```


### Lancer le projet :

On peut tester d'abord sans docker :
```
uv run python -m src.train

domain: data_protection
Modèle entraîné et sauvegardé : /home/***/ConformiteReglementaire_phase2/models/category_model_v1.json
```

```
uv run pytest  -q

=============================================== test session starts ===============================================
platform linux -- Python 3.13.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /home/***/ConformiteReglementaire_phase2
configfile: pyproject.toml
collected 4 items                                                                                                 

tests/test_characterization.py ....                                                                         [100%]

================================================ 4 passed in 0.01s ================================================
```

```
uv run python -m src.cli "Nous n'avons pas de DPO désigné mais traitons les données de 800 clients."

[{"regulation_id": "REG-008", "code": "DPO-2023", "domain": "data_protection", "criticality": "LOW", "validity": "valide", "status": "ok"}, {"regulation_id": "REG-011", "code": "DPO-2024", "domain": "data_protection", "criticality": "LOW", "validity": "valide", "status": "ok"}]
```

On peut tester ensuite sous docker :
```
docker compose run train

Image conformitereglementaire-train Built
Container conformitereglementaire_phase2-train-run-b348c3a53207 Creating 
Container conformitereglementaire_phase2-train-run-b348c3a53207 Created 
Modèle entraîné et sauvegardé : /app/models/category_model_v1.json
```

```
docker compose up --build app

[+] up 2/2
 ✔ Image conformitereglementaire_phase2-app       Built                                                        2.8s
 ✔ Container conformitereglementaire_phase2-app-1 Recreated                                                    0.3s
Attaching to app-1
app-1  | domain: data_protection
app-1  | [{"regulation_id": "REG-008", "code": "DPO-2023", "domain": "data_protection", "criticality": "LOW", "validity": "valide", "status": "ok"}, {"regulation_id": "REG-011", "code": "DPO-2024", "domain": "data_protection", "criticality": "LOW", "validity": "valide", "status": "ok"}]
app-1 exited with code 0

```
