# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True


# ajout de la fonction  constuireGrilleDemineur

def construireGrilleDemineur(n_lig: int, n_col: int):
    if n_col <= 0 or n_lig <= 0:
        raise ValueError(f"construireGrilleDemineur : Le nombre de lignes {n_lig} ou de colonnes {n_col} est négatif ou nul.")
    if type(n_col) != int or type(n_lig) != int:
        raise TypeError(f"construireGrilleDemineur : Le nombre de lignes {type(n_lig)} ou de colonnes {type(n_col)} n’est pas un entier. ")
    '''
    Donc ici on creer un grille resultat final du tableaux 2D 
    etage représente 1 ligne de la grille qui contient toute les cellule 
    etage après avoir  été remplie seras mis dans la grille avant d'etre vidé, plus on recommence.
    '''
    Grille=[]
    etage=[]
    for ligne in range(n_lig):
        for colone in range(n_col):
            etage.append(construireCellule())
        Grille.append(etage)
    return Grille


