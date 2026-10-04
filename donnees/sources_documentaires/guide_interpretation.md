# Guide d'interprétation — ACSI

**Guide officiel d'interprétation des règlements ACSI**

*Dernière mise à jour : 15 février 2024*

---

## 1. Clarifications sur les seuils

### 1.1 — Seuil RGD-2024 (500 personnes)

**Question** : Le seuil de 500 personnes pour l'obligation de DPO concerne-t-il les données actives ou les données archivées ?

**Réponse** : Le seuil concerne les **données actives** (traitées dans les 12 mois). Les données archivées ne sont pas comptabilisées.

**Exemple** : Une entreprise a 600 clients actifs et 2000 clients inactifs (pas de transaction depuis plus de 24 mois). Elle est soumise à l'obligation de DPO car elle traite des données de plus de 500 personnes.

---

### 1.2 — Seuil PCR-2022 (250 employés)

**Question** : Comment calculer le nombre d'employés pour le RTO ?

**Réponse** : Le calcul se fait sur l'effectif moyen annuel (ETP - Équivalent Temps Plein).

**Exemple** : Une entreprise compte 300 employés ETP. Elle est soumise au RTO de 24h (et non 72h).

---

## 2. Définition de "secteur critique" (DSI-2023)

### 2.1 — Liste des codes NAF concernés

Le "secteur critique" pour la DSI-2023 comprend les codes NAF suivants :

| Code NAF | Secteur |
|----------|---------|
| K64.* | Activités Financières |
| K65.* | Assurances |
| Q86.* | Activités pour la santé humaine |
| Q87.* | Hébergement médico-social |
| D35.* | Production/Distribution électricité/gaz/eau |
| H49.* | Transports terrestres |
| H50.* | Transports par eau |
| H51.* | Transports aérien

**Note** : Une entité est soumise si AU MOINS 50% de son activité correspond à un secteur critique.

---

## 3. Interprétation de "auditeur externe indépendant"

### 3.1 — Critères d'indépendance

Un auditeur est considéré comme indépendant si :

1. **Pas de relation capitalistique** : L'auditeur ou son groupe ne détient pas de participation dans l'entité auditée
2. **Pas de prestation de conseil dans les 24 mois** : L'auditeur n'a pas fourni de services de conseil (stratégie, implémentation, audit interne) dans les 24 mois précédant l'audit
3. **Pas de lien personnel** : Aucun lien familial ou amical avec la direction de l'entité

**Exemple concret** : Un cabinet qui a accompagné l'entité sur un projet de transformation digitale ne peut pas réaliser le pentest annuel.

---

## 4. Questions-réponses fréquentes

### Q1 : Une entité peut-elle avoir plusieurs DPO ?

**R** : Oui, si les activités sont distinctes (ex: groupe avec plusieurs filiales autonomes). Chaque entité juridique doit avoir son propre DPO ou un DPO mutualisé avec accord formalisé.

### Q2 : Le DPO peut-il être un prestataire externe ?

**R** : Oui, un DPO externe (prestataire) est autorisé. Il doit cependant être lié par un contrat définissant ses missions et sa disponibilité.

### Q3 : Les tests de pénétration doivent-ils être réalisés par un organisme certifié ?

**R** : Non, la réglementation ne mandate pas de certification spécifique mais impose l'indépendance et la compétence technique reconnue.

### Q4 : Comment calculer le délai de notification d'incident ?

**R** : Le délai court à partir du moment où l'entité a connaissance de l'incident (détection). Le moment de survenance n'entre pas en compte.

### Q5 : Le DPO peut-il être aussi首席信息官 (CIO) ?

**R** : Non, le DPO doit être indépendant. Il ne peut pas occuper un poste avec responsabilité opérationnelle sur les systèmes d'information.

### Q6 : Le chiffrement est-il obligatoire pour toutes les données ?

**R** : Non, seulement pour les données sensibles. Les données non sensibles (ex: liste des salles de réunion) ne nécessitent pas de chiffrement.

### Q7 : Quelle est la durée maximale de conservation des journaux d'accès ?

**R** : 1 an minimum, jusqu'à 3 ans pour les entités de secteur critique (DSI-2023, Art. 8).

### Q8 : Les sous-traitants sont-ils soumis aux mêmes obligations ?

**R** : Oui, si un sous-traitant traite des données pour le compte d'une entité soumise, il doit respecter les mêmes obligations. La responsabilité reste auprès de l'entité.

### Q9 : Un incident de sécurité doit-il toujours être notifié ?

**R** : Uniquement si l'incident a un impact sur les données personnelles ou la disponibilité des services critiques. Les incidents mineurs (ex: tentative d'intrusion bloquée) ne nécessitent pas de notification.

### Q10 : Le DPO doit-il être formé ?

**R** : Oui, le DPO doit disposer de connaissances suffisantes. L'ACSI recommande une formation initiale de 40h minimum et un recyclage annuel.

---

## 5. Décisions passées sur cas ambigus

### DEC-2023-047 — Absence de DPO

**Cas** : Une entreprise de 600 employés n'avait pas désigné de DPO en arguant que le traitement de données était sous-traité.

**Décision** : Non-conformité confirmée (Art. 18). La sous-traitance ne dispense pas de l'obligation de désignation. Amende : 150 000 €.

---

### DEC-2023-102 — Auditeur non indépendant

**Cas** : Une entité avait fait réaliser son pentest par un cabinet qui avait accompagné sa transformation digitale 6 mois auparavant.

**Décision** : Non-conformité confirmée (Art. 7). Le cabinet n'était pas indépendant. Nouvel audit exigé sous 3 mois.

---

### DEC-2024-011 — RTO pour grandes entités

**Cas** : Une entité de 2500 employés avait un RTO de 48h.

**Décision** : Non-conformité (Art. 2 PCR-2022). Pour les entités > 1000 employés, le RTO maximum est 24h. Délai de mise en conformité : 6 mois.

---

### DEC-2024-023 — Premier cas REG-007 sur IA de scoring

**Cas** : Une banque utilisait un algorithme de scoring crédit sans documentation d'explicabilité ni supervision humaine.

**Décision** : Non-conformité critique (Art. 6 et Art. 8 REG-007). Mise en conformité obligatoire avant septembre 2024.

---

## 6. Coordonnées

Pour toute question d'interprétation :
- Email : interpre@acsi.gouv.fr
- Téléphone : 01 XX XX XX XX (heures de bureau)
- Formulaire en ligne : https://www.acsi.gouv.fr/interrogation
