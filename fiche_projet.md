# Conformité Réglementaire

## Contexte métier

Le cabinet AuditPro accompagne des entités soumises aux règlements de l'ACSI, une autorité de contrôle fictive utilisée dans ce cas pédagogique. Les auditeurs croisent des textes réglementaires, des décisions passées et des éléments propres à chaque entité afin d'identifier des écarts, de prioriser les contrôles et de préparer leurs rapports.

Ce travail est exigeant : une conclusion doit pouvoir être expliquée, reliée à ses sources et revue par un professionnel compétent.

## Utilisateurs et enjeux

Les utilisateurs principaux sont les auditeurs. Les responsables de mission et les experts juridiques interviennent pour les interprétations sensibles et les conclusions engageantes.

Les enjeux sont d'accélérer la préparation des dossiers, de rendre les vérifications plus cohérentes et de garder une traçabilité utile. Les risques majeurs sont la mauvaise prise en compte de la temporalité d'un texte, une interprétation juridique abusive, une conclusion insuffisamment justifiée ou une absence d'escalade humaine.

## Données mises à disposition

Les jeux suivants sont fournis. Ils représentent des sources de travail ; leur sélection et leur rôle dans votre proposition font partie du cadrage.

- `donnees/sources_documentaires/reglement_rgd_2024.md` : règlement relatif à la gouvernance des données.
- `donnees/sources_documentaires/directive_securite_si.md` : directive relative à la sécurité des systèmes d'information.
- `donnees/sources_documentaires/guide_interpretation.md` : indications d'interprétation publiées par l'autorité compétente.
- `donnees/sources_documentaires/decisions_reference.md` : décisions et cas de référence antérieurs.
- `donnees/donnees_tabulaire/entities.csv` : caractéristiques et périmètres des entités auditées.
- `donnees/donnees_tabulaire/regulations.csv` : informations de suivi des règlements applicables.
- `donnees/donnees_tabulaire/controls.csv` : contrôles planifiés ou réalisés.
- `donnees/donnees_tabulaire/non_conformities.csv` : non-conformités identifiées.
- `donnees/donnees_tabulaire/risk_register.csv` : risques recensés par entité.
- `donnees/jeux_evaluation/eval_cases.csv` : cas de référence pour construire et exécuter votre évaluation.

## Contraintes réelles

- La validité temporelle des textes et des décisions doit être prise en compte.
- Une analyse doit pouvoir être reliée à des éléments vérifiables et conservée dans une trace exploitable.
- Les éléments fournis peuvent contenir des informations sensibles sur les entités auditées.
- Une interprétation juridique ou une conclusion engageante nécessite une validation humaine et un circuit d'escalade clair.

## Workflows métier actuels

### Préparer un dossier d'audit

**Déclencheur → acteurs → informations consultées → décisions → actions → résultat attendu**  
Ouverture d'une mission → auditeur, responsable de mission → profil de l'entité, règlements applicables, risques connus, contrôles précédents → choisir les thèmes à examiner et les éléments manquants → constituer un dossier de travail et planifier les contrôles → mission préparée et priorisée.

Frottements et risques observables : sources dispersées, texte applicable à une date incertaine, périmètre mal compris.

### Analyser un écart potentiel

**Déclencheur → acteurs → informations consultées → décisions → actions → résultat attendu**  
Élément d'audit collecté → auditeur, expert métier → pièce examinée, exigences applicables, guide d'interprétation, décisions comparables → estimer s'il existe un écart et son niveau de risque → rédiger une analyse sourcée ou demander une expertise → écart qualifié, justifié ou écarté.

Frottements et risques observables : interprétation ambiguë, analogie abusive avec un cas passé, justification insuffisante.

### Valider et communiquer une conclusion

**Déclencheur → acteurs → informations consultées → décisions → actions → résultat attendu**  
Conclusion provisoire → auditeur, responsable de mission, expert juridique si nécessaire → analyse, preuves, historique et registre des risques → décider de la formulation, de l'escalade et du niveau de confiance → un responsable humain valide le rapport ou demande une révision → conclusion traçable, compréhensible et communiquée selon le circuit prévu.

Frottements et risques observables : conclusion trop affirmative, oubli d'une réserve, communication non autorisée, perte de traçabilité.

## Votre cadrage

À partir de ces éléments, choisissez un objectif prioritaire et formulez un MVP observable. Quel problème précis mérite d'être traité en premier, pour quel utilisateur, et pourquoi ? Définissez une baseline, une métrique de succès et les sources réellement utiles. Précisez le niveau d'automatisation retenu, les risques, les garde-fous et les non-objectifs. Quelle décision doit rester humaine ? Quelle preuve vous ferait conclure que le MVP aide réellement sans accroître le risque ?

Justifiez explicitement pourquoi un **traitement LLM simple (chat)**, un **Workflow**, un **RAG** ou un **Agent** sont retenus ou écartés pour votre périmètre — la solution la plus simple qui fait la preuve de la valeur est un choix légitime. Explicitez notamment la manière dont vous maîtrisez la temporalité, la traçabilité et la validation humaine.

## Démarrer

Commencez par la [méthodologie unifiée AI Engineering](../../AI_engineering_project_message/README.md). Elle vous guide du cadrage à l'exploitation et rappelle les bonnes pratiques de software engineering attendues.

Documentez vos décisions importantes dans des ADR et conservez les preuves demandées à chaque phase : contrat, baseline, tests, résultats d'évaluation, traces et démonstrations de fonctionnement ou d'échec maîtrisé.

Le jeu de 5 à 10 cas demandé dès le cadrage peut partir des cas fournis dans `donnees/jeux_evaluation/` ; complétez-les par vos propres cas ambigus et d'erreur, en documentant ce que vous ajoutez et pourquoi.
