NOTES

 1 Environnement d'exécution

- Projet : AgendaCampus
- exécution  : Python seul avec Uvicorn
- Commande utilisée :
  ```bash
  python -m uvicorn app.main:app --reload
  ```
- Version de Python : python 3.14.3
- Adresse de l'application : http://127.0.0.1:8000/

 Problèmes rencontrés et solutions

- petit embrouille sur l;execution des commandes pour lancer l'application
- disposition des differentes pages
- comprehension de jinja2 

 Partie B 

Adresse testée : `http://127.0.0.1:8000/`

Dans l'onglet Réseau  des outils de développement du navigateur, j'ai observé les requêtes suivantes :

| Méthode |      Adresse             | Code HTTP  | Content-Type |

| GET     | `http://127.0.0.1:8000/` |   200      |   html       |
| GET     | `/static/css/style.css` |    200      |   css        |
| GET     | `http://127.0.0.1:8000/favicon.ico`   |    404       |     json    |

2 Test des  adresses inexistantes

- Adresse testée : `http://127.0.0.1:8000/nexiste/pas`
- Code HTTP  : [404]
- Contenu du corps : not found, il ne trouve pas l'evenement

3 Documentation FastAPI

- Adresse : `http://127.0.0.1:8000/docs`
- La documentation interactive de FastAPI permet de consulter et de tester les différentes routes de l'application.
- La route `/api/sante` a été testée avec le bouton « Try it out ».

4 Tests avec curl

Commande GET :
- Résultat de la requête GET : HTTP/1.1 200 ok
- Résultat de la requête POST : HTTP/1.1 404 method not  allowed
- 405: la ;ethode n'est pas autorise; 404 la page est introuvable



 Partie D : Tests de la page de détail

Les trois adresses demandées dans la fiche TD/TP ont été testées.

| Adresse testée      | Code HTTP attendu |                 Explication                                              |

| `/evenements/1`     |    200            | L'événement ayant l'identifiant 1 existe                                 |
| `/evenements/999`   |    404            | La route existe, mais aucun événement ne possède cet identifiant.        |
| `/evenements/abc`   |    422            | L'identifiant fourni n'est pas un entier, hors un entier.                |

Test du formulaire d'inscription

- Adresse POST : `/evenements/1/inscription`
- Code HTTP : 404
- Explication : il ne trouve pqs de page c;est normal car il n'existe pas encore de base 

4 Test d'accessibilité au clavier

Le test a été effectué sans utiliser la souris, avec les touches suivantes :

- `Tab` : passer à l'élément suivant.
- `Maj + Tab` : revenir à l'élément précédent.
- `Entrée` : activer un lien ou un bouton.
Observations :
- les liens et les champs sont accessibles au clavier
- le focus reste visible pendant la navigation
- les corrections effectuées, si nécessaire

