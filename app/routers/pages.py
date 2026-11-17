"""Pages HTML rendues côté serveur (Jinja2), séance 1 : point de départ."""
from fastapi import APIRouter, Request

from app.donnees import EVENEMENTS, trouver_evenement
from app.templating import templates

router = APIRouter()


@router.get("/api/sante")
def sante():
    # Une route qui renvoie du JSON : FastAPI convertit le dictionnaire.
    return {"statut": "ok"}


@router.get("/")
def accueil(request: Request):
    evenements_tries = sorted(
    EVENEMENTS,
    key=lambda e: e["debut"]
    )

    return templates.TemplateResponse(
        request,
        "index.html",
        {"evenements": evenements_tries}
    )




# TODO (fiche TD/TP, partie D) : route GET /evenements/{evenement_id}
#   - utiliser trouver_evenement() du module app.donnees


@router.get("/evenements/{evenement_id}")
def detail_evenement(request: Request, evenement_id: int):
    evenement = trouver_evenement(evenement_id)

    if evenement is None:
        return templates.TemplateResponse(
            request,
            "404.html",
            {"request": request},
            status_code=404
        )

    return templates.TemplateResponse(
        request,
        "evenement.html",
        {"evenement": evenement}
    )

#   - rendre evenement.html si l'événement existe
#   - sinon rendre 404.html avec le code de statut 404
