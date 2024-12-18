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
    #option
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
        etage=[]
        for colonne in range(n_col):
            etage.append(construireCellule())
        Grille.append(etage)
    return Grille


#ajout de getNbLigneGrilleDelineur
def getNbLignesGrilleDemineur(grille:list):
    if not type_grille_demineur(grille):
        raise TypeError(f" getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille)
#ajout de getNbColonnesGrilleDemineur
def getNbColonnesGrilleDemineur(grille:list):
    if not type_grille_demineur(grille):
        raise TypeError(f" getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return  len(grille[0])

#ajout isCoordonneeCorrecte

def isCoordonneeCorrecte(grille:list,coordonnee:tuple):
    #option
    if not  grille == list and coordonnee == tuple:
        raise TypeError(f" isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    #code
    return (getNbLignesGrilleDemineur(grille)-1) >= coordonnee[0] and (getNbColonnesGrilleDemineur(grille)-1)>= coordonnee[1]
# ici si les coo sont belle est bien compris dans le tableaux


#ajout getCelluleGrilleDemineur

def getCelluleGrilleDemineur(grille:list,coo:tuple):
    if not  grille == list and coo == tuple:
        raise TypeError(f"getCelluleGrilleDemineur : un des paramètres n’est pas du bon type")
    if not isCoordonneeCorrecte(grille,coo):
        raise IndexError(f"getCelluleGrilleDemineur : coordonnée non contenue dans la grille")
    return grille[coo[0]][coo[1]]

#ajout getContenuGrilleDemineur

def getContenuGrilleDemineur(grille:list,coo:tuple):
    cellule=getCelluleGrilleDemineur(grille,coo)
    return getContenuCellule(cellule)

#ajout setContenuGrilleDemineur

def setContenuGrilleDemineur(grille:list,coo:tuple,newcontenu:int):
    cellule=getCelluleGrilleDemineur(grille,coo)
    setContenuCellule(cellule,newcontenu)
    return


#ajout isVisibleGrilleDemineur

def isVisibleGrilleDemineur(grille:list,coo:tuple,):
    cellule = getCelluleGrilleDemineur(grille, coo)
    return isVisibleCellule(cellule)

#ajout setVisibleGrilleDemineur

def setVisibleGrilleDemineur(grille:list,coo:tuple,newvisible:bool):
    cellule = getCelluleGrilleDemineur(grille, coo)
    setVisibleCellule(cellule,newvisible)
    return

def contientMineGrilleDemineur(grille:list,coo:tuple):
    cellule = getCelluleGrilleDemineur(grille, coo)
    return contientMineCellule(cellule)



# Ici on va commencer les fonction neccesaire a la mise en place du jeux.

def getCoordonneeVoisinsGrilleDemineur(grille:list,coo:tuple):
    #option
    if type(grille) != list or type(coo) != tuple:
        raise TypeError(f"getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type")
    if not isCoordonneeCorrecte(grille,coo):
        raise IndexError(" getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille.")
    #code
    voisin=[]
    for ligne in range((coo[0])-1,(coo[0])+2):
        for colone in range ((coo[1]-1),(coo[1]+2)):
            if (ligne >= 0 and colone >= 0):
                coordonner = construireCoordonnee(ligne, colone)
                if isCoordonneeCorrecte(grille,coordonner) and (coordonner != coo):
                    voisin.append(coordonner)
    return voisin

#ajout de placerMineGrilleDemineur

def placerMinesGrilleDemineur(grille:list,nb:int,coord:tuple):
    #option
    if nb<= 0 or nb>=(getNbLignesGrilleDemineur(grille)*getNbColonnesGrilleDemineur(grille)):
        raise ValueError (f" placerMinesGrilleDemineur : Nombre de bombes à placer incorrect")
    if not isCoordonneeCorrecte(grille,coord):
        raise IndexError(f"placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille.")
    #code
    coord_mines = []
    #création de la liste qui seris de sauvegarde et de nombre de boucle
    while len(coord_mines) != nb:
        mine = (randint(0, getNbLignesGrilleDemineur(grille)), randint(0, getNbColonnesGrilleDemineur(grille)))
        #selection d'un cellule aléatoire
        if mine != coord and not mine in coord_mines and isCoordonneeCorrecte(grille, mine):

            coord_mines.append(mine)
            cell = getCelluleGrilleDemineur(grille, mine)
            setContenuCellule(cell, const.ID_MINE)
            # ajout a la suvegarde + comodification de la cellule
    compterMinesVoisinesGrilleDemineur(grille)
    return

#ajout de compterMinesVoisinesGrilleDemineur
def compterMinesVoisinesGrilleDemineur(grille:list):
    for ligne in range(getNbLignesGrilleDemineur(grille)):
        for colonne in range(getNbColonnesGrilleDemineur(grille)):
            # pour obtenir les cood
            nb_mine_autour = 0
            # va remplacer le contenue a la fin
            if not contientMineGrilleDemineur(grille,construireCoordonnee(ligne,colonne)):
                # verifie si la cellele n'est pas un mine
                voisin=getCoordonneeVoisinsGrilleDemineur(grille,construireCoordonnee(ligne,colonne))
                for voisin_x in voisin:
                    # parcout les voisin pour trouver les mine
                    if contientMineGrilleDemineur(grille,voisin_x):
                        nb_mine_autour+=1
                setContenuGrilleDemineur(grille,construireCoordonnee(ligne,colonne),nb_mine_autour)
    return

#ajour de la fonction  getNbMinesGrilleDemineur
def getNbMinesGrilleDemineur( grille:list)->int:
    if not type_grille_demineur(grille):
        raise ValueError(f"getNbMinesGrilleDemineur : le paramètre n’est pas une grille")
    mine_total=0
    for ligne in range(getNbLignesGrilleDemineur(grille)):
        for colonne in range(getNbColonnesGrilleDemineur(grille)):
            #a noter que je suis obliger d'avoir des cooordonne pour utiliser contientMinesGrilleDemineur
            if contientMineGrilleDemineur(grille,construireCoordonnee(ligne,colonne)):
                mine_total+=1
    return mine_total

#ajout getAnnotationGrilleDemineur
def getAnnotationGrilleDemineur(grille:list,coord:tuple):
    cellule = getCelluleGrilleDemineur(grille, coord)
    return getAnnotationCellule(cellule)


def getMinesRestantesGrilleDemineur(grille):
    nb_mine=getNbMinesGrilleDemineur(grille)
    nb_flag=0
    for ligne in range(getNbLignesGrilleDemineur(grille)):
        for colonne in range(getNbColonnesGrilleDemineur(grille)):
            # a noter que je suis obliger d'avoir des cooordonne pour utiliser la fonction
            if getAnnotationGrilleDemineur(grille,construireCoordonnee(ligne,colonne)) == const.FLAG:
                nb_flag+=1
    return nb_mine -nb_flag

def gagneGrilleDemineur(grille):
    gagner=True
    for ligne in range(getNbLignesGrilleDemineur(grille)):
        for colonne in range(getNbColonnesGrilleDemineur(grille)):
            # a noter que je suis obliger d'avoir des cooordonne pour utiliser la fonction
            coo=construireCoordonnee(ligne,colonne)
            if not contientMineGrilleDemineur(grille,coo):
                if isVisibleGrilleDemineur(grille,coo) == False :
                    gagner = False
            elif isVisibleGrilleDemineur(grille,coo) == True:
                gagner = False
    return gagner

def perduGrilleDemineur(grille):
    perdu = False
    for ligne in range(getNbLignesGrilleDemineur(grille)):
        for colonne in range(getNbColonnesGrilleDemineur(grille)):
            # a noter que je suis obliger d'avoir des cooordonne pour utiliser la fonction
            coo = construireCoordonnee(ligne, colonne)
            if contientMineGrilleDemineur(grille, coo) and isVisibleGrilleDemineur(grille, coo) == True:
                perdu = True
    return perdu
def reinitialiserCellule(cell):
    cell[const.CONTENU]= 0
    cell[const.VISIBLE] = False
    cell[const.ANNOTATION]= None
    return
def reinitialiserGrilleDemineur(grille):
    for ligne in grille:
        for cell in ligne:
            reinitialiserCellule(cell)
    return
def decouvrirGrilleDemineur(grille:list,coord:tuple):
    decouvert=set(coord)
    setVisibleGrilleDemineur(grille, coord, True)
    voisinage=getCoordonneeVoisinsGrilleDemineur(grille,coord)
    for voisin in voisinage:
        if getContenuGrilleDemineur(grille, voisin) == 0 and isVisibleGrilleDemineur(grille,voisin) == False:
           decouvert.update(decouvrirGrilleDemineur(grille,voisin))
    return decouvert


