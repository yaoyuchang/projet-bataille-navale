# bateau.py

class Bateau:
    """
    Représente un bateau placé sur la grille.
    - ligne, colonne : position de départ
    - longueur : taille du bateau (défaut = 1)
    - vertical : orientation (False = horizontal, True = vertical)
    """

    def __init__(self, ligne: int, colonne: int, longueur: int = 1, vertical: bool = False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical
        self.marque = "⛵"  # 默认通用小船

    @property
    def positions(self):
        """
        Retourne la liste des positions occupées par le bateau.
        Format : liste de tuples (ligne, colonne)
        Tri :
        - horizontal → colonne 递增
        - vertical → ligne 递增
        """
        pos = []
        if self.vertical:
            for i in range(self.longueur):
                pos.append((self.ligne + i, self.colonne))
        else:
            for i in range(self.longueur):
                pos.append((self.ligne, self.colonne + i))
        return pos
    
    def coule(self, grille) -> bool:
        """
        Vérifie si le bateau est coulé sur la grille donnée.
        Un bateau est coulé si toutes ses cases sont marquées '💣'.
        """
        for (ligne, colonne) in self.positions:
            idx = ligne * grille.n_colonnes + colonne
            if grille.matrice[idx] != "💣":
                return False
            else:
                continue
        return True


# 仍然在 bateau.py 里，放在 Bateau 类后面

class PorteAvion(Bateau):
    """Porte-avion de longueur 4, marque 🚢."""

    def __init__(self, ligne: int, colonne: int, vertical: bool = False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical)
        self.marque = "🚢"


class Croiseur(Bateau):
    """Croiseur de longueur 3, marque ⛴."""

    def __init__(self, ligne: int, colonne: int, vertical: bool = False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical)
        self.marque = "⛴"


class Torpilleur(Bateau):
    """Torpilleur de longueur 2, marque 🚣."""

    def __init__(self, ligne: int, colonne: int, vertical: bool = False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
        self.marque = "🚣"


class SousMarin(Bateau):
    """Sous-marin de longueur 2, marque 🐟."""

    def __init__(self, ligne: int, colonne: int, vertical: bool = False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
        self.marque = "🐟"
