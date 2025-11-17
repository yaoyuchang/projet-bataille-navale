'''g = Grille(5, 8)
print(g)
g.tirer(2, 3)
print(g)'''

# main.py

import random
from grille import Grille
from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin


def chevauchent(b1: Bateau, b2: Bateau) -> bool:
    """Vérifie si deux bateaux se chevauchent (ont au moins une case en commun)."""
    return bool(set(b1.positions).intersection(b2.positions))


def placer_bateaux_aleatoirement(grille: Grille):
    """
    Place un porte-avion, un croiseur, un torpilleur et un sous-marin
    aléatoirement sur la grille, sans chevauchement.
    Retourne la liste des bateaux placés.
    """
    bateaux = []
    # 按题目顺序：航母、巡洋舰、鱼雷艇、潜艇
    types_bateaux = [PorteAvion, Croiseur, Torpilleur, SousMarin]

    for BateauType in types_bateaux:
        placements_possibles = []

        for ligne in range(grille.n_lignes):
            for colonne in range(grille.n_colonnes):
                for vertical in (False, True):
                    # 创建一个临时船，看看它是否在网格内且不与已有船重叠
                    b = BateauType(ligne, colonne, vertical=vertical)

                    # 1) 检查是否完全在网格内
                    positions = b.positions
                    dans_grille = all(
                        0 <= li < grille.n_lignes and 0 <= co < grille.n_colonnes
                        for (li, co) in positions
                    )
                    if not dans_grille:
                        continue

                    # 2) 检查是否与已有船重叠
                    chevauche = any(chevauchent(b, autre) for autre in bateaux)
                    if chevauche:
                        continue

                    placements_possibles.append((ligne, colonne, vertical))

        if not placements_possibles:
            raise RuntimeError("Impossible de placer tous les bateaux sans chevauchement.")

        # 随机选择一个合法位置
        ligne, colonne, vertical = random.choice(placements_possibles)
        b_def = BateauType(ligne, colonne, vertical=vertical)
        # 在 grille 的 matrice 里用 marque 标记位置（虽然 print 时玩家会看到，但符合题目前面 Grille.ajoute 的要求）
        #grille.ajoute(b_def)
        bateaux.append(b_def)
        # 注意：这里不再调用 grille.ajoute(b_def)
        # 这样玩家一开始看不到船的位置

    return bateaux


def demander_coordonnees(grille: Grille):
    """
    Demande à l'utilisateur une paire (ligne, colonne) valide.
    """
    while True:
        try:
            ligne_str = input(f"Entrez la ligne (0 à {grille.n_lignes - 1}) : ")
            colonne_str = input(f"Entrez la colonne (0 à {grille.n_colonnes - 1}) : ")
            ligne = int(ligne_str)
            colonne = int(colonne_str)

            if not (0 <= ligne < grille.n_lignes and 0 <= colonne < grille.n_colonnes):
                print("Coordonnées hors de la grille, réessayez.")
                continue

            return ligne, colonne
        except ValueError:
            print("Entrée invalide, veuillez entrer des nombres entiers.")


def trouver_bateau_touche(bateaux, ligne, colonne):
    """
    Renvoie le bateau qui occupe la case (ligne, colonne), ou None s'il n'y en a pas.
    """
    for b in bateaux:
        if (ligne, colonne) in b.positions:
            return b
    return None


def afficher_message_coule(bateau: Bateau):
    """Affiche un message spécifique selon le type de bateau coulé."""
    if isinstance(bateau, PorteAvion):
        print("💥 Vous avez coulé le porte-avion !")
    elif isinstance(bateau, Croiseur):
        print("💥 Vous avez coulé le croiseur !")
    elif isinstance(bateau, Torpilleur):
        print("💥 Vous avez coulé le torpilleur !")
    elif isinstance(bateau, SousMarin):
        print("💥 Vous avez coulé le sous-marin !")
    else:
        print("💥 Vous avez coulé un bateau !")


def jeu_bataille_navale():
    # 1) 创建 8x10 的网格
    grille = Grille(8, 10)

    # 2) 随机放置 4 艘不同类型的船
    bateaux = placer_bateaux_aleatoirement(grille)

    # 统计玩家射击次数（只统计有效的新射击）
    nb_coups = 0

    print("Bienvenue dans la bataille navale !")
    print("Tentez de couler les 4 bateaux cachés sur la grille.\n")

    # 3) 游戏主循环
    while True:
        print("\nGrille actuelle :")
        print(grille)
        print("-------------------------")

        # 3.1 玩家输入坐标
        ligne, colonne = demander_coordonnees(grille)

        idx = ligne * grille.n_colonnes + colonne
        case_actuelle = grille.matrice[idx]

        # 3.2 已经打过的格子
        if case_actuelle == "x":
            print("Vous avez déjà tiré sur cette case, choisissez-en une autre.")
            continue

        nb_coups += 1  # 只统计新的射击

        # 3.3 检查是否击中船
        bateau_touche = trouver_bateau_touche(bateaux, ligne, colonne)

        if bateau_touche is not None:
            print("💣 Touché !")
            # 在该格子标记为 x（击中）
            grille.tirer(ligne, colonne, touche="💣")

            # 3.4 检查这艘船是否已经被击沉
            if bateau_touche.coule(grille):
                afficher_message_coule(bateau_touche)
                # 把整艘船显示为它的 marque
                for (li, co) in bateau_touche.positions:
                    idx_b = li * grille.n_colonnes + co
                    grille.matrice[idx_b] = bateau_touche.marque
        else:
            print("🌊 À l'eau !")
            # 没打中船，标记为 x
            grille.tirer(ligne, colonne, touche="x")

        # 3.5 检查游戏是否结束（所有船都已击沉）
        tous_coules = all(b.coule(grille) for b in bateaux)
        if tous_coules:
            print("\n🎉 Félicitations ! Vous avez coulé tous les bateaux.")
            print(f"Nombre de coups nécessaires : {nb_coups}")
            print("\nGrille finale :")
            print(grille)
            break


if __name__ == "__main__":
    jeu_bataille_navale()
