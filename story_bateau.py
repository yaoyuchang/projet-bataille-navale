# story_bateau.py

from bateau import Bateau


def chevauchent(b1: Bateau, b2: Bateau) -> bool:
    """
    Vérifie si deux bateaux se chevauchent.
    """
    # positions 是 list[tuple]
    p1 = set(b1.positions)
    p2 = set(b2.positions)
    return len(p1.intersection(p2)) > 0


def story_chevauchement():
    print("User Story : chevauchement")
    print("--------------------------")

    print("\nCas 1 : bateaux qui se chevauchent")
    b1 = Bateau(2, 3, longueur=3)                 # positions : (2,3),(2,4),(2,5)
    b2 = Bateau(2, 4, longueur=2)                 # positions : (2,4),(2,5)
    print("B1 :", b1.positions)
    print("B2 :", b2.positions)
    print("Chevauchent ? ", chevauchent(b1, b2))

    print("\nCas 2 : bateaux qui ne se chevauchent pas")
    b3 = Bateau(0, 0, longueur=2)
    b4 = Bateau(1, 0, longueur=3)
    print("B3 :", b3.positions)
    print("B4 :", b4.positions)
    print("Chevauchent ? ", chevauchent(b3, b4))


if __name__ == "__main__":
    story_chevauchement()
