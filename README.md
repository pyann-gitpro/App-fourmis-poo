
# Jeu de Morpion (version 0.2 with test)

Ce projet est un simple jeu de Morpion en Python avec une interface d'affichage graphique de la grille à l'aide de `matplotlib`. Le jeu se joue à deux joueurs et s'arrête lorsqu'un joueur gagne ou lorsque la partie se termine par un match nul.

## Modules

Le projet est organisé en plusieurs modules :

1. **game.py** : Le fichier principal qui contrôle le déroulement du jeu. Il utilise les fonctions des autres modules pour gérer la grille, les réponses des joueurs et la vérification des conditions de victoire ou de match nul.

2. **reponse.py** : Ce module gère les entrées des joueurs. Il demande à l'utilisateur d'entrer la ligne et la colonne où il souhaite placer son marqueur (X ou O).

3. **grid.py** : Ce module contient la grille du jeu et une fonction pour afficher la grille à l'aide de `matplotlib`.

4. **victoire_nul.py** : Ce module contient les fonctions qui vérifient si un joueur a gagné ou si le match est nul.

## Prérequis

- Python 3.x
- Les bibliothèques suivantes doivent être installées :
    - `numpy`
    - `matplotlib`

Vous pouvez installer ces bibliothèques avec la commande suivante :

```bash
pip install -r requirements.txt
```

## Exécution du jeu

Pour démarrer le jeu, exécutez simplement le fichier `game.py` :

```bash
python game.py
```

Le jeu affichera la grille à chaque tour, et les joueurs devront entrer les numéros de ligne et de colonne pour placer leur marqueur. Le jeu continue jusqu'à ce qu'un joueur gagne ou qu'il y ait match nul.

## Structure des fichiers

Voici l'arborescence du projet :

```bash
.
├── !!!à créer (.github)/
│        ├──workflows/
│               ├── tests.yml/
├── .venv/
├── public/
|       ├──module/
│       │       ├── __pycache__/
│       │       ├── grid.py
│       │       ├── reponse.py
│       │       └── victoire_nul.py
│       ├── !!!à créer (tests)/
│               ├── __pycache__/
│               └── test_morpion.py
├── app.py
├── .gitignore
├── README.md
├── requirements.txt
```

## Généralités

Cette application simule une colonie de fourmis composée de différentes classes : ouvrières, soldats et une reine. Chaque fourmi effectue des actions comme collecter de la nourriture, défendre la colonie ou produire de nouvelles fourmis. L'énergie de la colonie est partagée et est consommée lorsque les fourmis se déplacent.

## Tests Unitaires / Github Actions et Workflows

- **Créer un fichier de workflow** : Dans votre dépôt GitHub, créez un fichier `.github/workflows/tests.yml` (ou un nom similaire). Ce fichier YAML définit les étapes de votre workflow d'automatisation.
- **Définir les déclencheurs** : Indiquez quand vous souhaitez que vos tests soient exécutés (par exemple, à chaque push sur la branche main, lors de la création d'une pull request, etc.).
- **Configurer l'environnement** : Spécifiez l'environnement d'exécution de vos tests (système d'exploitation, version de Python, dépendances, etc.).
- **Exécuter les tests** : Utilisez les actions appropriées pour installer vos dépendances, puis lancez vos tests avec la commande de votre framework de test (pytest, unittest, etc.).
- **Afficher les résultats** : Utilisez les actions pour afficher les résultats des tests directement sur GitHub, par exemple en les publiant dans les commentaires de la pull request.

***Voici un exemple simple de workflow pour pytest :***

```yaml
name: Python application CI/CD
on:
  push:
    branches: [ main, dev ]  # Branch to survey
  pull_request:
    branches: [ main ]
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11"]
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements_train.txt
        # Add any specific installation commands for libcpab
        pip install -e libcpab


    # tests
    - name: Run unit tests (un fichier)
      run: |
        pytest tests/test_0.py
    - name: Run unit tests (un autre fichier)
      run: |
        pytest tests/test_1.py
```

## Créateurs

- [Saadia CHADLI](mailto:@gmail.com)
- [Jules NDIAYE](mailto:@gmail.com)
- [Yann PAAEHO](mailto:paaeho.yann.pro@gmail.com)







#### Projet colonie de fourmis
#### Groupe poulpe : Saadia, Yann, Jules

# Fourmis Simulation App
## Description

##### Cette application simule une colonie de fourmis composée de différentes classes : ouvrières, soldats et une reine. Chaque fourmi effectue des actions comme collecter de la nourriture, défendre la colonie ou produire de nouvelles fourmis. L'énergie de la colonie est partagée et est consommée lorsque les fourmis se déplacent.
Prérequis

    Python 3.x doit être installé sur votre machine.
    Pour vérifier que Python est installé, vous pouvez exécuter la commande suivante dans un terminal :

    bash

    python --version

    Modules supplémentaires : Aucun module externe n'est requis pour cette application, vous pouvez utiliser les bibliothèques standard de Python.

Installation

    Clonez ce dépôt ou copiez le code source dans votre projet local :

    bash

git clone <URL_du_dépôt>

Accédez au répertoire du projet :

bash

    cd <nom_du_répertoire>

Lancement de l'application

    Exécutez le script principal fourmis.py dans un terminal pour démarrer la simulation :

    bash

    python app.py

    L'application simule les actions des fourmis dans la colonie, et affiche les résultats tels que la nourriture collectée, les nouvelles fourmis produites, et l'énergie restante de la colonie.

Best Practices
1. Structure du code

    Organisation des classes : Le code est organisé en trois classes principales qui héritent de la classe mère Fourmi. Cela permet une modularité et facilite les évolutions futures de l'application.
        Ouvriere : Responsable de la collecte de nourriture.
        Soldat : Défend la colonie.
        Reine : Produit de nouvelles fourmis.

    Méthodes de classe (@classmethod) : La méthode se_deplacer est utilisée avec le décorateur @classmethod pour représenter une action globale qui affecte l'énergie partagée par la colonie.

2. Ajout de fonctionnalités

    Facilité d'ajout de nouvelles actions : Si vous souhaitez ajouter de nouvelles actions pour une fourmi (par exemple, exploration), vous pouvez simplement définir une nouvelle méthode dans les sous-classes concernées.

    Attributs partagés : L'attribut energie_class est un bon exemple d'attribut partagé au niveau de la classe, garantissant que toutes les instances accèdent à la même ressource énergétique.

3. Gestion de l'énergie

L'énergie est un élément clé dans cette simulation. Chaque action de déplacement réduit l'énergie de la colonie entière. Assurez-vous de suivre l'état de l'énergie via la méthode se_deplacer.

4. Modularité et réutilisabilité

    Si vous voulez réutiliser ce projet ou l'étendre à d'autres types d'insectes, vous pouvez facilement le faire en ajoutant de nouvelles sous-classes à la classe mère Fourmi.
    La gestion de la nourriture et des nouvelles fourmis est conçue pour être flexible et adaptable à des scénarios plus complexes.

Débogage

Si vous rencontrez des erreurs lors de l'exécution du script, assurez-vous que vous utilisez la bonne version de Python et que le code source est correctement copié.