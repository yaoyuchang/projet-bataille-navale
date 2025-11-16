# test_bateau.py

from bateau import Bateau
from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin

def test_positions_horizontal():
    b = Bateau(2, 3, longueur=3)
    assert b.positions == [(2, 3), (2, 4), (2, 5)]

def test_positions_vertical():
    b = Bateau(2, 3, longueur=3, vertical=True)
    assert b.positions == [(2, 3), (3, 3), (4, 3)]
def test_ajoute_bateau_hors_grille():
    g = Grille(2, 3)
    # 这个纵向放的话会出界（需要行 1,2），而最大行索引是 1
    b1 = Bateau(1, 0, longueur=2, vertical=True)
    g.ajoute(b1)

    # 这个长度 4 肯定出界
    b2 = Bateau(1, 0, longueur=4, vertical=True)
    g.ajoute(b2)

    # 网格应该保持全是 ∿
    assert g.matrice == ["∿", "∿", "∿", "∿", "∿", "∿"]