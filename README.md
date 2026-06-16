# LITReview

LITReview est une application web de réseau social dédiée aux critiques de livres et d'articles. Elle permet aux utilisateurs de demander des critiques, d'en publier, et de consulter celles des personnes qu'ils suivent.

---

## Fonctionnalités

### Trois cas d'utilisation principaux

- **Demander une critique** : créer un ticket pour signaler qu'un livre ou un article mérite d'être lu et/ou solliciter l'avis de la communauté.
- **Publier une critique** : rédiger une critique en réponse à un ticket existant, ou directement en créant le ticket et la critique en une seule fois.
- **Explorer les critiques** : consulter un fil d'actualité personnalisé affichant les tickets et critiques des utilisateurs suivis, ainsi que les réponses reçues sur ses propres tickets.

### Gestion du compte et du réseau

- Inscription et connexion sécurisées
- Suivi d'autres utilisateurs (follow/unfollow)
- Visualisation de ses abonnements et abonnés
- Modification et suppression de ses propres tickets et critiques

---

## Prérequis

- **Python 3.10 ou supérieur**
- **pip**

Vérifier la version de Python installée :

```bash
python3 --version
```

---

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/Volgar3/OC_P9.git
cd <nom-du-dossier>
```

### 2. Créer et activer un environnement virtuel

#### macOS / Linux

```bash
python3 -m venv env
source env/bin/activate
```

#### Windows (PowerShell)

```powershell
python -m venv env
env\Scripts\Activate.ps1
```

> Une fois activé, le nom de l'environnement `(env)` apparaît au début de la ligne de commande.

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer le serveur de développement

```bash
python manage.py runserver
```

L'application est accessible à l'adresse : [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Comptes de test

La base de données `db.sqlite3` fournie contient des données de test ainsi que les comptes suivants :

| Nom d'utilisateur | Mot de passe | Rôle        |
|-------------------|--------------|-------------|
| `hugo2`           | `hugo2`      | Admin       |
| `volgar`          | `volgar`     | Utilisateur |
| `Alice`           | `Alice`      | Utilisateur |
| `Bob`             | `Bob`        | Utilisateur |

> Le compte `hugo2` donne accès à l'interface d'administration Django via [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

---

## Structure du projet

```
projet_n°9/
├── env/                        # Environnement virtuel Python
└── litReview/                  # Répertoire principal du projet Django
    ├── authentication/         # Application : authentification utilisateurs
    │   ├── models.py           # Modèle User personnalisé
    │   ├── views.py            # Vues : login, logout, inscription
    │   └── forms.py            # Formulaires d'authentification
    ├── social_network/         # Application : tickets, critiques, abonnements
    │   ├── models.py           # Modèles : Ticket, Review, UserFollows
    │   ├── views.py            # Vues : fil d'actualité, CRUD tickets/critiques
    │   └── forms.py            # Formulaires
    ├── config/                 # Configuration Django
    │   ├── settings.py
    │   └── urls.py
    ├── templates/              # Templates HTML (base + pages)
    ├── static/                 # Fichiers statiques (CSS, images)
    ├── db.sqlite3              # Base de données SQLite avec données de test
    ├── manage.py
    └── requirements.txt        # Dépendances Python
```

---

## Stack technique

| Technologie       | Version  | Usage                                 |
|-------------------|----------|---------------------------------------|
| Python            | 3.10+    | Langage principal                     |
| Django            | 6.0.4    | Framework web                         |
| SQLite            | —        | Base de données                       |
| django-bootstrap5 | 26.2     | Mise en page responsive               |
| Pillow            | 12.2.0   | Gestion des images de couverture      |

---

## Désactiver l'environnement virtuel

Une fois terminé, désactiver l'environnement avec :

```bash
deactivate
```

---

## Tester le site

Un compte utilisateur de test est disponible pour explorer l'application :

| Champ             | Valeur |
|-------------------|--------|
| Nom d'utilisateur | `Bob`  |
| Mot de passe      | `Bob`  |

Ce compte dispose de tickets et de critiques existants, ce qui permet de voir le fil d'actualité alimenté dès la connexion.
