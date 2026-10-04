"""Tests de caractérisation : 

Ces tests protègent le contrat observable, pas l'implémentation :
- le schéma de la réponse (les trois clés, toujours présentes)
- les domaines et criticités autorisés
- le refus propre sur message vide ou hors périmètre

Ils ne figent JAMAIS la formulation exacte d'un texte libre : si le
mock est un jour remplacé par un vrai modèle, ces tests doivent
continuer à passer tant que le contrat est respecté.
"""

import json
from pathlib import Path

from src.classify import classify

DOMAIN = {"data_governance", "cybersecurity", "business_continuity", "audit", "cloud", "ai_governance", "data_protection", "incident_management", "data_retention"}
CRITICALITY = {"HIGH", "MEDIUM", "LOW"}

TEST_CASES = [
    json.loads(line)
    for line in (Path(__file__).parent.parent / "donnees/tests" / "test_set_v1.jsonl")
    .read_text(encoding="utf-8")
    .splitlines()
    if line.strip()
]


def test_cas_nominal_respecte_le_contrat():
    result = classify("Nous n'avons pas de DPO désigné mais traitons les données de 800 clients.")
    assert isinstance(result, list)
    # une liste d'un seul élément
    assert len(result) == 2
    for regulation in result:
        assert regulation["regulation_id"]
        assert regulation["code"]
        assert regulation["domain"] in DOMAIN
        assert regulation["status"] == "ok"
        assert regulation["criticality"] in CRITICALITY


def test_message_vide_est_refuse_proprement():
    result = classify("")
    assert isinstance(result, list)
    assert len(result) == 1
    result = result[0]
    assert result["regulation_id"] is None
    assert result["code"] is None
    assert result["domain"] is None
    assert result["criticality"] is None
    assert result["status"] == "needs_review"


def test_message_hors_perimetre_est_refuse_proprement():
    result = classify("??? 1234")
    assert isinstance(result, list)
    assert len(result) == 1
    result = result[0]
    assert result["regulation_id"] is None
    assert result["code"] is None
    assert result["domain"] is None
    assert result["criticality"] is None
    assert result["status"] == "needs_review"


def test_le_jeu_de_test_versionne_respecte_le_contrat():
    for case in TEST_CASES:
        #print("[test contrat]: ligne=", case)
        result = classify(case["message"])
        assert isinstance(result, list) 

        for regulation in result:
            #print("[test contrat]: ", regulation)
            assert regulation["status"] == case["expected_status"]
            if regulation["status"] == "ok":
                assert regulation["domain"] == case["expected_domain"], case["message"]
                assert regulation["criticality"] in CRITICALITY
            else:
                assert regulation["domain"] is None
                assert regulation["criticality"] is None
