# Projet Bataille Navale

Un jeu interactif de bataille navale implémenté en Python, avec gestion des grilles, des bateaux et une boucle de gameplay complète.

## ✨ Fonctionnalités

- **Grille de jeu** : Matrice 8×10 pour placer et cibler les bateaux
- **Placement aléatoire** : 4 types de bateaux placés automatiquement sans chevauchement
  - Porte-avion (longueur 4) 🚢
  - Croiseur (longueur 3) ⛴
  - Torpilleur (longueur 2) 🚣
  - Sous-marin (longueur 2) 🐟
- **Gameplay interactif** : Saisissez les coordonnées pour tirer
- **Suivi du jeu** : Détection des touches, coulage de bateaux et affichage de la grille
- **Tests automatisés** : Suite de tests avec pytest

## 🏗️ Architecture

### Modules principaux

- **`grille.py`** : Classe `Grille` gérant la matrice, les tirs et l'affichage
- **`bateau.py`** : Classe `Bateau` et sous-classes spécialisées pour chaque type
- **`main.py`** : Boucle de gameplay, placement des bateaux et interaction utilisateur

### Tests et User Stories

- **`test_grille.py`** : Tests unitaires pour la classe Grille
- **`test_bateau.py`** : Tests unitaires pour la classe Bateau
- **`story_grille.py`** : User story "Plouf dans l'eau"
- **`story_bateau.py`** : User story "Chevauchement"

## 📦 Installation

### Prérequis

- Python 3.13+
- pip

### Étapes

1. **Clonez ou accédez au répertoire du projet**
   ```bash
   cd projet-bataille-navale
   ```

2. **Créez une environnement virtuel (si non existant)**
   ```bash
   python3 -m venv .venv
   ```

3. **Activez l'environnement virtuel**
   ```bash
   source .venv/bin/activate
   ```

4. **Installez les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Utilisation

### Lancer le jeu

```bash
python main.py
```

Le jeu vous demandera des coordonnées (ligne et colonne) pour tirer sur la grille. Objectif : couler tous les 4 bateaux en le moins de coups possible !

## 🧪 Tests

### Exécuter un fichier de test spécifique

```bash
pytest test_grille.py -v
pytest test_bateau.py -v
```

### Exécuter un test spécifique

```bash
pytest test_grille.py::test_init -v
```

## 🔧 Dépendances

Voir `requirements.txt` pour la liste complète.

- Les positions des bateaux sont stockées sous forme de listes de tuples `(ligne, colonne)`
- La grille interne est une liste 1D ; l'indice est calculé comme `ligne * n_colonnes + colonne`
- Les caractères spéciaux représentent les états : `∿` (vide), `x` (tiré), emojis (bateaux coulés)

Projet éducatif pour le cours ECM INFO.
