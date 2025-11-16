# grille.py
from bateau import Bateau

class Grille:
    """Représente une grille de bataille navale sans bateaux (pour l'instant)."""

    def __init__(self, n_lignes: int, n_colonnes: int):
        """
        Crée une grille vide de n_lignes x n_colonnes.
        La grille est stockée dans une liste 1D de taille n_lignes * n_colonnes.
        Chaque case est initialement remplie avec le caractère '∿' (vide).
        """
        self.n_lignes = n_lignes
        self.n_colonnes = n_colonnes
        self.vide = "∿"
        # matrice : liste 1D, index = ligne * n_colonnes + colonne
        self.matrice = [self.vide] * (n_lignes * n_colonnes)

    def _index(self, ligne: int, colonne: int) -> int:
        """Calcule l'indice dans la liste pour la case (ligne, colonne)."""
        if not (0 <= ligne < self.n_lignes and 0 <= colonne < self.n_colonnes):
            raise ValueError(f"Coordonnées hors grille : ({ligne}, {colonne})")
        return ligne * self.n_colonnes + colonne

    def tirer(self, ligne: int, colonne: int, touche: str = "x") -> None:
        """
        Marque un tir sur la case (ligne, colonne) avec le caractère `touche`.
        Par défaut, on utilise 'x' pour représenter un tir.
        """
        idx = self._index(ligne, colonne)
        self.matrice[idx] = touche

    def __str__(self) -> str:
        """
        Retourne une représentation textuelle de la grille.
        Chaque ligne est une chaîne de caractères, les lignes sont séparées par des sauts de ligne.
        """
        lignes = []
        for i in range(self.n_lignes):
            # extrait la sous-liste correspondant à la ligne i
            debut = i * self.n_colonnes
            fin = debut + self.n_colonnes
            ligne = "".join(self.matrice[debut:fin])
            lignes.append(ligne)
        return "\n".join(lignes)
    
    def ajoute(self, bateau) -> None:
        """
        Place un bateau sur la grille en remplaçant les caractères
        par bateau.marque (par défaut '⛵') aux positions du bateau.
        On ne fait la modification que si le bateau rentre entièrement
        dans la grille.
        """
        positions = bateau.positions

        # 1. 检查是否完全在网格内
        for (ligne, colonne) in positions:
            if not (0 <= ligne < self.n_lignes and 0 <= colonne < self.n_colonnes):
                # 船超出边界 -> 不做任何修改
                return

        # 2. 全部合法 -> 放船
        for (ligne, colonne) in positions:
            idx = ligne * self.n_colonnes + colonne
            self.matrice[idx] = bateau.marque