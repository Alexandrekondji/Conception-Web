"""Données de la séance 1, écrites en dur dans le code.

C'est volontaire : aujourd'hui on se concentre sur HTTP, HTML et CSS.
La séance 2 remplacera cette liste par une vraie couche métier, et la
séance 3 par une base de données.
"""
from datetime import datetime, timedelta

_aujourdhui = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

EVENEMENTS = [
    {
        "id": 1,
        "titre": "Atelier Git pour débutants",
        "description": "Versionner son code, créer un dépôt, faire ses premiers commits.",
        "lieu": "LAB1",
        "debut": _aujourdhui + timedelta(days=2, hours=14),
        "capacite": 25,
        "inscrits": 18,
    },
    {
        "id": 2,
        "titre": "Conférence : le métier de développeur web",
        "description": "Échanges avec d'anciens étudiants de la faculté.",
        "lieu": "Amphithéâtre principal",
        "debut": _aujourdhui + timedelta(days=5, hours=10),
        "capacite": 120,
        "inscrits": 37,
    },
    {
        "id": 3,
        "titre": "Tournoi de football inter-facultés",
        "description": "Inscription individuelle ; les équipes seront formées sur place.",
        "lieu": "Stade du campus",
        "debut": _aujourdhui + timedelta(days=9, hours=15, minutes=30),
        "capacite": 44,
        "inscrits": 44,
    },
]


def trouver_evenement(evenement_id: int) -> dict | None:
    for evenement in EVENEMENTS:
        if evenement["id"] == evenement_id:
            return evenement
    return None
