# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0


# Ajout de la fonction construireCoordonner

def construireCoordonnee(n_ligne: int ,n_col:int):
    # option
    if not (type(n_col)== int and type(n_ligne)==int):
        raise TypeError(f"construireCoordonnee : Le numéro de ligne {type(n_ligne)} ou le numéro de colonne {type(n_col)} ne sont pas des entiers")
    if not n_ligne >= 0 and n_col >= 0:
        raise ValueError(f"construireCoordonnee : Le numéro de ligne {n_ligne} ou de colonne {n_col} sont pas positifs")
    return (n_ligne,n_col)

# ajout de la fonction getligneCoordonnee

def getLigneCoordonnee(coordonner_tuple:tuple):
    # option
    if  not (len(coordonner_tuple)== 2 and  type(coordonner_tuple) == tuple and (type(coordonner_tuple[0])== int and type(coordonner_tuple[1])==int)):
        raise TypeError ("getLigneCoordonnee : Le paramètre n’est pas une coordonnée")
    return coordonner_tuple[0]
# ajout de la fonction getColonneCoordonnee
def getColonneCoordonnee(coordonner_tuple:tuple):
    # option
    if not (len(coordonner_tuple)== 2 and type(coordonner_tuple) == tuple and  (type(coordonner_tuple[0]) == int and type(coordonner_tuple[1])==int)):
        raise TypeError ("getLigneCoordonnee : Le paramètre n’est pas une coordonnée")
    return coordonner_tuple[1]