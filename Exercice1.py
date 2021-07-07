# -*-coding:Utf-8 -*


def intCheck(): # Demande une saisie d'entier et la renvoie
    try:
        nombre = int(input("Saisissez un entier : "))
    except ValueError:
        print("Votre suggestion n'était pas un entier") # Si la saisie n'est pas un entier, on met fin à l'appel
        print("Le programme se termine ici.")
        quit()
    return nombre

def reelCheck(): # Demande une saisie d'entier et la renvoie
    try:
        nombre = float(input("Veuillez maintenant saisir un réel : "))
    except ValueError:
        print("Votre suggestion n'était pas un réel")
        print("Le programme se termine ici.")
        quit()
    return nombre

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

## 1. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est positif (>= 0) ou non, et affiche
# “positif” ou “négatif”.
def exo1():

    nombre = intCheck()
    if (type(nombre) != int):
        print("Ceci n'est pas un nombre")
    elif (nombre >= 0):
        print("Ceci est un nombre positif")
    else:
        print("Ceci est un nombre négatif")

#exo1()

## 2. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est strictement positif, nul ou strictement
# négatif, et affiche ce résultat.

def exo2():

    nombre = intCheck()
    if (nombre > 0):
        print("Ceci est un nombre strictement positif")
    elif (nombre == 0):
        print("Ceci est un nombre nul")
    else:
        print("Ceci est un nombre négatif")

#exo2()


## 3. Écrire un algorithme qui demande un réel à l’utilisateur et affiche sa valeur absolue (sans utiliser de fonction
# prédéfinie évidemment).

def exo3():
    n_reel = reelCheck()
    abs_n_reel = n_reel
    if (n_reel < 0):
        abs_n_reel *= -1
    # abs_n_reel est maintenant forcément positif : la valeur absolue de n_reel
    print(abs_n_reel)

#exo3()

## 4. Écrire un algorithme qui demande un réel à l’utilisateur et l’arrondit à l’entier le plus proche (les x,5 seront arrondis
# à l’entier supérieur).

def exo4():
    n_reel = reelCheck()
    n_cut = int(n_reel)
    delta = n_reel - n_cut
    if (delta > 0.5) and (n_reel >= 0):
        n_arrondi = n_cut + 1
    elif (-delta > 0.5) and (n_reel < 0):
        n_arrondi = n_cut - 1
    else:
        n_arrondi = n_cut

    print(n_arrondi)

#exo4()

## 5. Écrire un algorithme qui demande le numéro d’un mois et affiche le nombre jours que comporte ce mois (sans tenir
# compte des années bissextiles).

def exo5():
    print("Nous vous demandons ici un chiffre de mois 1-12")
    mois = intCheck()
    if (mois < 1) or (mois > 12):
        print("Ceci ne correspond pas à un mois")
        quit()

    if (mois in [1,3,5,7,8,10,12]):
        print("Ce mois comporte 31 jours")
    elif (mois == 2):
        print("Ce mois comporte 28 jours")
    else:
        print("Ce mois comporte 30 jours")

#exo5()


## 6. Écrire un algorithme qui vérifie si une année est bissextile. On rappelle qu’il y a des années bissextiles tous les
# 4 ans, mais la première année d’un siècle ne l’est pas (1800, 1900 n’étaient pas bissextiles) sauf tous les 400 ans
# (2000 était une année bissextile).

def exo6():
    print("Nous vous demandons ici d'entrer une année")
    annee = intCheck()

    # J'avais oublié % = modulo
    if is_integer(annee/4): # Si on a bien une année divisible par 4
        if not is_integer(annee/ 100):
            print("Ceci est une année bisextile")
        elif is_integer(annee/ 400 ):
            print("Ceci est une année bisextile")
        else:
            print("Ceci n'est pas une année bisextile")
    else:
        print("Ceci n'est pas une année bisextile")

#exo6()


## 7. Écrire un algorithme qui demande une date sous la forme de 2 nombres entiers (numéro du jour et numéro du mois)
# et affiche la saison (ex : 12/02; hiver). On supposera que le premier jour de la saison est toujours le 21.


# On suppose ici que personne ne nous donne des valeurs abberantes par facilité

def exo7():
    print("Nous vous demandons ici d'entrer un jour 0-28") # Pour passer les exceptions si le changement est toujours le 21
    jour = intCheck()
    print("Et maintenant un mois 1-12")
    mois = intCheck()

    if (jour >= 21 and mois == 12) or mois == 1 or mois == 2 or (jour < 21 and mois == 3):
        print("Hiver")
    elif (jour >= 21 and mois == 3) or mois == 4 or mois == 5 or (jour < 21 and mois == 6):
        print("Printemps")
    elif (jour >= 21 and mois == 6) or mois == 7 or mois == 8 or (jour < 21 and mois == 9):
        print("Eté")
    elif (jour >= 21 and mois == 9) or mois == 10 or mois == 11 or (jour < 21 and mois == 12):
        print("Automne")

exo7()


