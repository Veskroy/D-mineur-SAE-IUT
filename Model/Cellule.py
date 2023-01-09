# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


#ajout fonction iscontenueCorrect

def isContenuCorrect(nombre: int):
    # option
    return (type(nombre)== int and (nombre >= 0 and nombre <= 8))or nombre == const.ID_MINE

#ajoute de la fontion construirecellule

def construireCellule(int_contenue = 0, bool_visible = False):
    #Option
    if not isContenuCorrect(int_contenue):
        raise ValueError (f"construireCellule : le contenu {int_contenue} n’est pas correct ")
    if not type(bool_visible)== bool:
        raise TypeError (f" construireCellule : le second paramètre {type(bool_visible)} n’est pas un booléen")
    Cellule = {const.CONTENU: int_contenue, const.VISIBLE : bool_visible}
    return Cellule
