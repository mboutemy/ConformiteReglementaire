# Décisions de référence — ACSI

**Recueil des décisions significatives de l'ACSI**

*Année 2023-2024*

---

## DEC-2023-047 — Absence de DPO (RGD-2024, Art. 18)

**Date** : 15 septembre 2023

**Entité** : [Anonymisée] — Entreprise du secteur logistique, 600 employés

**Faits** : L'entité ne avait pas désigné de Délégué à la Protection des Données alors qu'elle traitait les données de plus de 800 clients et 200 employés.

**Motif de l'entité** : L'entité arguait que le traitement de données était entièrement sous-traité à un prestataire, et que ce dernier disposait d'un DPO.

**Décision** : Non-conformité confirmée.

**Motif** : La désignation d'un DPO est une obligation directe de l'entité contrôlée, non transférable au sous-traitant. La responsabilité reste auprès du responsable de traitement.

**Sanction** : Amende de 150 000 € + mise en conformité sous 3 mois.

**Précedent** : Cette décision crée un précédent sur le fait que la sous-traitance ne dispense pas de l'obligation de désignation du DPO.

---

## DEC-2023-102 — Auditeur non indépendant (DSI-2023, Art. 7)

**Date** : 20 novembre 2023

**Entité** : [Anonymisée] — Entreprise du secteur énergie, 1200 employés

**Faits** : L'entité avait fait réaliser son test de pénétration annuel par un cabinet d'audit qui avait accompagné sa transformation digitale 6 mois auparavant.

**Motif de l'entité** : Le cabinet disposait d'une expertise reconnue et l'entitéestimait que le critère d'indépendance était rempli car aucun lien capitalistique n'existait.

**Décision** : Non-conformité confirmée.

**Motif** : Le cabinet avait fourni des services de conseil (stratégie et implémentation) dans les 24 mois précédant l'audit. Le critère d'indépendance n'était pas respecté.

**Sanction** : Nouvel audit obligatoire sous 3 mois par un auditeur indépendant + rappel à la réglementation.

**Précedent** : Cette décision clarifie que la notion d'indépendance inclut l'absence de prestation de conseil dans les 24 mois.

---

## DEC-2024-011 — RTO insuffisant pour grande entité (PCR-2022, Art. 2)

**Date** : 10 janvier 2024

**Entité** : [Anonymisée] — Groupe de la grande distribution, 2500 employés

**Faits** : L'entité avait documenté un RTO (Recovery Time Objective) de 48 heures pour ses systèmes critiques.

**Motif de l'entité** : L'entitéconsidérait que 48h était un objectif réaliste compte tenu de la complexité de ses systèmes.

**Décision** : Non-conformité HIGH.

**Motif** : L'Art. 2 du PCR-2022 impose un RTO maximum de 24 heures pour les entités de plus de 1000 employés.

**Sanction** : Mise en conformité obligatoire sous 6 mois + plan d'action détaillé.

**Précedent** : Cette décision confirme que le seuil de 1000 employés est un seuil absolu, sans exception.

---

## DEC-2024-023 — IA de scoring crédit sans explicabilité (REG-007, Art. 6 et Art. 8)

**Date** : 5 mars 2024

**Entité** : [Anonymisée] — Établissement financier, secteur fintech

**Faits** : L'entité utilisait un modèle de scoring automatique pour l'attribution de crédit. Les décisions étaient entièrement automatisées, sans relecture humaine ni possibilité de contestation explicative.

**Motif de l'entité** : Le modèle était basé sur des critères objectifs et le taux de réponse positive était élevé.

**Décision** : Non-conformité CRITICAL.

**Motif** : 
- Art. 6 : Absence de documentation d'explicabilité (XAI) du modèle
- Art. 8 : Absence de mécanisme de supervision humaine sur les décisions automatisées

**Sanction** : Mise en conformité obligatoire avant le 30 septembre 2024 (date d'entrée en vigueur effective du REG-007) + amendes potentielles en cas de non-conformité.

**Précedent** : Premier cas traité relatif au REG-007 (Règlement IA). Cette décision établit les attentes de l'ACSI en matière d'IA responsable.

---

## DEC-2024-045 — Conservation excessive de données (RGD-2024, Art. 15)

**Date** : 20 février 2024

**Entité** : [Anonymisée] — Entreprise retail, 3200 clients

**Faits** : L'entité conservait les données clients pendant 10 ans après la fin de la relation contractuelle, pour des raisons commerciales.

**Motif de l'entité** : La conservation long-terme permettait des analyses marketing et des campagnes de fidélisation.

**Décision** : Non-conformité HIGH.

**Motif** : L'Art. 15 du RGD-2024 impose une durée maximale de conservation de 5 ans pour les données clients. La conservation pour des finalités autres que celles initiales n'est pas许可ée.

**Sanction** : Suppression des données excédant 5 ans sous 3 mois + procédure de purge automatique à mettre en place.

---

## DEC-2024-056 — Chiffrement insuffisant (DSI-2023, Art. 8)

**Date** : 10 mars 2024

**Entité** : [Anonymisée] — Compagnie d'assurance, secteur financier

**Faits** : La base de données des sinistres contenait des données sensibles non chiffrées au repos.

**Motif de l'entité** : Le chiffrement était en cours de déploiement et l'entitéestimait que les mesures de sécurité physiques étaient suffisantes.

**Décision** : Non-conformité HIGH.

**Motif** : L'Art. 8 de la DSI-2023 rend le chiffrement des données sensibles obligatoire au repos, sans exception.

**Sanction** : Projet de chiffrement en phase de spécification + audit de sécurité additionnel.

---

## Synthèse des principes dégagés

| Principe | Source | Portée |
|----------|--------|--------|
| La sous-traitance ne dispense pas du DPO | DEC-2023-047 | Art. 18 RGD-2024 |
| Indépendance = pas de conseil dans 24 mois | DEC-2023-102 | Art. 7 DSI-2023 |
| RTO 24h pour > 1000 employés | DEC-2024-011 | Art. 2 PCR-2022 |
| IA = XAI + supervision humaine obligatoire | DEC-2024-023 | Art. 6 et 8 REG-007 |
