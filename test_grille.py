import pytest
from grille import Grille


def test_init():
    g = Grille(5, 8)
    assert g.n_lignes == 5
    assert g.n_colonnes == 8
    # 一维列表长度 = 5 * 8 = 40
    assert len(g.matrice) == 5 * 8
    # 所有格子都等于 vide
    assert all(cell == g.vide for cell in g.matrice)

def test_tirer_marks_cell():
    g = Grille(5, 8)
    g.tirer(2, 3)  # 第 3 行第 4 列（从 0 开始）
    idx = 2 * g.n_colonnes + 3
    assert g.matrice[idx] == "x"


def test_afficher_str_shape():
    g = Grille(2, 3)
    s = str(g)

    lignes = s.split("\n")
    # 应该有 2 行
    assert len(lignes) == 2
    # 每行长度 = 3 列
    assert all(len(ligne) == 3 for ligne in lignes)
