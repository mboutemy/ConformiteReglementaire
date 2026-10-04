# Conformité Réglementaire : Phase 2

## 4 décisions à prendre avant de coder
### 1. Liste fermée

Domain = Literal["data_governance", "cybersecurity", "business_continuity", "audit", "cloud", "ai_governance", "data_protection", "incident_management", "data_retention"]

Criticality = Literal["CRITICAL", "HIGH", "MEDIUM", "LOW"]

Cas needs_review :
- si l'input est vide ou hors périmètre
- s'il n'y a pas de réglementation identifiée
- si plusieurs domaines sont possibles
- si les dates de réglementaires ne s'appliquent pas
- si on passe un Domain différent de la liset fermée à ClassificationResult

### 2. Cas ambigu
Dans le cas :
EVAL-C5,"Nous avons un plan de continuité validé en 2022. Notre RTO est de 48h. Nous avons 1200 employés.",REG-003,Art.2,CRITICAL,"Test NC continuité - RTO insuffisant pour taille entité"

On sait que la REG-003 Protocole de Continuité et Résilience 2022 s'applique de 01/01/2022 à 01/01/2024 pour les entités > 250 employés. 
<span style="color:red"><strong>Mais on ne sait pas ce qu'il en est maintenant en 2026.</strong></span>

<span style="color:red"><strong>Aussi la citicité est MEDIUM. Alors que dans l'EVAL-C5, il est indiqué CRITICAL.</strong></span>

Comme il y a incohérence ou doute, on doit remonter le status `needs_review`.

### 3. Artefact
L'artefact est les mots clés par domain. Cela permet de classer un message par domaine. Il sera produit par le job d'entrainement mocké src/train.py

### 4. Cycles de vie
- ce qui tourne parfois ou quand les données input changent (données tabulaires ou sources documentaires):
Le classement des mots clés par domain.

- ce qui tourne toujours :
La classification des messages en entrée


## livrable
### 1. Contrat Pydantic
cf src/contracts.py

liste fermée de valeurs (Domain et Criticality) et statut de refus `needs_review`

### 2. Test de caractérisation qui porte sur le contrat
tests/test_characterization.py contient les tests de vérification de contrat.

### 3. Un jeu de test versionné
Le jeu de test de base est donnees/tests/test_set_v1.jsonl

### 4. Un run noté dans experiments/runs.jsonl 
création de src/train.py qui génère models/category_model_v1.json via la commande :
`uv run python -m src.train`

### 5. job séparé produit un artefact versionné
- **Job** : `src/train.py` (`uv run python -m src.train`). 

Il tourne *parfois*  quand il y a une modification sur un domaine, une réglementation ou les mots-clés.

- **Artefact** : `models/category_model_v1.json` (nom du modèle, version, date
  d'entraînement, domaine avec ses mots-clés).

- **Consommateur** : `MLCategoryModel` (`src/category_model.py`) doit charger cet artefact à la création de l'image Docker. 
  Les deux cycles de vie ne communiquent que par le fichier.

### 6. Sortie du prompt dans un fichier 
Le prompt qui était codé en dur dans classify._build_prompt() et mis dans prompts/classify_v1.txt

### 7. Dockerfile et docker-compose
voici les commandes à exéctuer :
```
docker compose run train
docker compose up --build app
```
`run train ` génère le fichier category_model_v1.json en local dans le répertoire models
`up --build app` gérnère l'output :
```
 ✔ Image conformitereglementaire_phase2-app       Built                                                                     1.6s
 ✔ Container conformitereglementaire_phase2-app-1 Created                                                                   0.2s
Attaching to app-1
app-1  | domain: data_protection
app-1  | [{"regulation_id": "REG-008", "code": "DPO-2023", "domain": "data_protection", "criticality": "LOW", "validity": "valide", "status": "ok"}, {"regulation_id": "REG-011", "code": "DPO-2024", "domain": "data_protection", "criticality": "LOW", "validity": "valide", "status": "ok"}]
app-1 exited with code 0
```

### 8. reproductibilité grâce au README
[Voir la section Installation et lancement](README.md#installation-et-lancement)

### 9. Tools
Développement de 3 tools : [Voir la description des tools](TOOLS.md)

