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

def construireCellule(int_contenue = 0, visible = False, annotation=None):
    #Option
    if not isContenuCorrect(int_contenue):
        raise ValueError (f"construireCellule : le contenu {int_contenue} n’est pas correct ")
    if not type(visible)== bool:
        raise TypeError (f" construireCellule : le second paramètre {type(visible)} n’est pas un booléen")
    Cellule = {const.CONTENU: int_contenue, const.VISIBLE: visible,const.ANNOTATION: annotation}
    return Cellule


# ajoout de la fonction getCOntenuecellule get Visible cellule

def getContenuCellule(cellule:dict):
    # option
    if not type_cellule(cellule):
        raise TypeError (f"getContenuCellule : Le paramètre n’est pas une cellule")
    return cellule[const.CONTENU]


def isVisibleCellule(cellule:dict):
    # option
    if not type_cellule(cellule):
        raise TypeError (f" isVisibleCellule: Le paramètre n’est pas une cellule")
    return cellule[const.VISIBLE]

#set contenue cellule

def setContenuCellule (cellule:dict, contenu: int):
    #option ** Je vais corriger le testcellue pour corriger les faute **.
   if not isContenuCorrect(contenu):
        raise ValueError (f'setContenuCellule : la valeur du contenu {contenu} n’est pas correcte')
   if not type_cellule(cellule):
       raise TypeError(f"setContenuCellule : Le premier paramètre n’est pas une cellule")

# ici vu que IsContuecorect verifie deja si contenu est un entier ca ne sert a rien de la mettre
   if type(contenu) != int:
       raise TypeError(f" setContenuCellule : Le second paramètre n’est pas un entier")
   cellule[const.CONTENU] =contenu
   return


# ajout de setvisible Cellule

def setVisibleCellule(cellule:dict,visible:bool):
    if not type_cellule(cellule):
        raise TypeError(f" setVisibleCellule: Le premier paramètre n’est pas une cellule")
    if type(visible) != bool:
        raise TypeError(f" setVisibleCellule : Le second paramètre n’est pas un booléen")
    cellule[const.VISIBLE] = visible
    return


# ajout de contientMineCellule
def contientMineCellule(cellule:dict):
    # option
    if not type_cellule(cellule):
        raise TypeError(f" contientMineCellule : Le  paramètre n’est pas une cellule")
    Reponse= False
    if cellule[const.CONTENU]== const.ID_MINE:
        Reponse = True # si il y a un mine on répond VRAi
    return Reponse # TRUE == il y a une bombe FALSE == il n'y en a pas

def isAnnotationCorrecte(anot:str)-> bool:
    result=False
    if anot== None or anot == const.DOUTE or anot== const.FLAG :
        result=True
    return result

def  getAnnotationCellule(cell):
    if not type_cellule(cell):
        raise TypeError(f"getAnnotationCellule : le paramètre {cell} n’est pas une cellule")
    if not const.ANNOTATION in cell:
        return None
    return cell[const.ANNOTATION]

def  changeAnnotationCellule(cell):
    if not type_cellule(cell):
        raise TypeError(f"getAnnotationCellule : le paramètre  n’est pas une cellule")
    if getAnnotationCellule(cell) == None:
        cell[const.ANNOTATION]=const.FLAG
    elif getAnnotationCellule(cell) == const.FLAG:
        cell[const.ANNOTATION] = const.DOUTE
    elif getAnnotationCellule(cell) == const.DOUTE:
        cell[const.ANNOTATION] = None
    return