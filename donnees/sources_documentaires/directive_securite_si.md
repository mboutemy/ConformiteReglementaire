# Directive Sécurité des Systèmes d'Information 2023 (DSI-2023)

**Autorité de Contrôle des Systèmes d'Information (ACSI)**

*Entrée en vigueur : 1er juillet 2023*

---

## Article 4 — Périmètre d'application

### 4.1 — Entités concernées

La présente directive s'applique aux entités de **secteur critique** :
- Santé (établissements de santé, laboratoires, pharma)
- Énergie (producteurs, transporteurs, distributeurs)
- Finance (banques, assurances, établissements de paiement)
- Transports (transporteurs aériens, ferrovaires, maritimes)
- Services essentiels (télécommunications, eau, alimentation)

### 4.2 — Définition de secteur critique

Est considérée comme entrant dans le périmètre toute entité dont le code NAF correspond à :
- Section K (finance et assurance)
- Section Q (santé humaine et action sociale)
- Section D (production et distribution d'énergie)
- Section H (transports et entreposage)

---

## Article 7 — Tests de pénétration

### 7.1 — Obligation annuelle

Toute entité soumise à la présente directive doit faire réaliser un **test de pénétration** de ses systèmes d'information par un auditeur externe indépendant.

### 7.2 — Fréquence

Le test doit être réalisé au minimum **une fois par an** et à chaque modification substantielle de l'architecture.

### 7.3 — Indépendance de l'auditeur

L'auditeur doit être **indépendant** de l'entité auditée :
- Pas de relation capitalistique
- Pas de prestation de conseil dans les 24 mois précédant l'audit
- Pas de même groupe industriel

**Sanction** : Test réalisé par un auditeur non indépendant ou non réalisé constitue une non-conformité critique (NC-010).

---

## Article 8 — Chiffrement des données

### 8.1 — Chiffrement au repos

Toutes les données sensibles doivent être chiffrées lorsqu'elles sont stockées (at-rest).

Les algorithmes utilisés doivent être conformes aux standards reconnus (AES-256, RSA-4096).

### 8.2 — Chiffrement en transit

Toutes les communications de données sensibles doivent être chiffrées (in-transit) via TLS 1.2 minimum.

### 8.3 — Gestion des clés

Les clés de chiffrement doivent être gérées selon les meilleures pratiques :
- Stockage dans un HSM ou vault dédié
- Rotation annuelle obligatoire
- Sauvegarde sécurisée

**Sanction** : Données sensibles non chiffrées au repos constitue une non-conformité HIGH (NC-016).

---

## Article 9 — Segmentation réseau

### 9.1 — Principe

L'entité doit mettre en place une **segmentation réseau** permettant d'isoler les zones de sensibilité différente.

### 9.2 — Zones à séparer

Au minimum, les zones suivantes doivent être distinctes :
- Zone administrative (bureaux, outils productivité)
- Zone de production (systèmes critiques)
- Zone démilitarisée (DMZ)
- Zone guest (visiteurs)

### 9.3 — Contrôles aux frontières

Chaque zone doit être protégée par des contrôles aux frontières (firewall, filtrage).

**Sanction** : Segmentation insuffisante entre zones critiques constitue une non-conformité critique (NC-009).

---

## Article 11 — Test du plan de réponse aux incidents

### 11.1 — Simulation obligatoire

Le plan de réponse aux incidents cyber doit être **testé** au minimum **une fois par an** via une simulation (table-top ou-live).

### 11.2 — Documentation

Le test doit être documenté avec :
- Scénario de simulation
- Résultats observés
- Actions correctives identifiées
- Plan d'action avec échéances

### 11.3 — Mise à jour

Le plan doit être mis à jour à chaque test et en cas d'incident réel.

**Sanction** : Plan non testé depuis plus de 18 mois constitue une non-conformité HIGH (NC-005).

---

## Article 14 — Notification d'incidents

### 14.1 — Délais de notification

| Severity de l'incident | Délai de notification ACSI |
|------------------------|---------------------------|
| CRITICAL | 24 heures |
| MAJOR | 48 heures |
| MINOR | 72 heures |

### 14.2 — Contenu de la notification

La notification doit contenir :
- Description de l'incident
- Données concernées (volume, nature)
- Mesures prises ou envisagées
- Impact potentiel

### 14.3 — Rapport détaillé

Un rapport détaillé doit être transmis dans les 15 jours suivant la notification initiale.

**Sanction** : Notification dépassant le délai constitue une non-conformité MEDIUM (NC-002).

---

## Dispositions finales

La présente directive entre en vigueur le 1er juillet 2023.

*Fait à Paris, le 15 juin 2023*
*Le Collège de l'ACSI*
