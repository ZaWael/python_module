# -*-coding:Utf-8 -*

###########################################################
# Liste des symboles utiles:
# =     : affectation
#
# Tests logiques (renvoient True si la condition testée est rencontrée, False sinon)
# ==    : est égal à
# !=    : est différent de
# >     : est supérieur à
# <     : est inférieur à
# >=    : est supérieur ou égal à
# <=    : est inférieur ou égal à
#
# Opérateurs logiques dans une expression logique
# and   : A and B renvoie True si A et B valent True
# or    : A or B renvoie True si au moins une des 2 condition est True
# not   : not(A) renvoie True si A est False, renvoie False si A == True
#
# Dans une chaine de caractère, le symbole \ est un caractère d'echappement
# qui dit à python de ne pas interpréter le caractère qui suit le symbole \ :
# \n    : permet un retour à la ligne (newline)
# \"    : pour ajouter le caractère " dans une chaine de caractère où le symbole " est reservé à sa définition
###########################################################

######################################################################################################################
# exemple de saisie et d'affichage de données à l'écran
######################################################################################################################
i = 0
if i != 0:
    texte = input("Saisir du texte (valider avec la touche \"Entrée\")\n")
    print("le texte saisi est " + texte + "\n")


a = "texte"

l=[0, 1, 2, 3, 4, 5]
dico = {'computer':'ordinateur', 'mouse':'souris',  'keyboard':'clavier'}
for key in dico.values():
    print(key)

