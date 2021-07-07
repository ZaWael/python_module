# -*-coding:Utf-8 -*

def intCheck(): # Demande une saisie d'entier et la renvoie
    try:
        nombre = int(input("Saisissez un entier positif : "))
    except ValueError:
        print("Votre suggestion n'était pas un entier") # Si la saisie n'est pas un entier, on met fin à l'appel
        print("Le programme se termine ici.")
        quit()
    return nombre

## 1. Écrire un algorithme qui demande un entier positif, et le rejette tant que le nombre saisi n’est pas conforme.

def exo1():
    nombre = intCheck()
    while nombre < 0:
        print("Le nombre saisi n'est pas conforme, réessayez")
        nombre = intCheck()
    print("Le nombre", nombre, "est bien un entier positif.")

exo1()

## 2. Écrire un algorithme qui demande 10 entiers, compte le nombre d’entiers positifs saisis, et affiche ce résultat.

def exo2():
    count = 0
    for i in range(10):
        print("Vous pouvez entrer nimporte quel nombre, seuls les positifs sont comptés")
        num = intCheck()
        if num >= 0:
            count +=1
    print("Vous avez saisi", count, "entiers positifs")

#exo2()

## 3. Écrire un algorithme qui demande des entiers positifs à l’utilisateur, les additionne, et qui s’arrête en affichant le
# résultat dès qu’un entier négatif est saisi.

def exo3():
    sum = 0
    num = 0
    while num >= 0:
        sum = sum + num
        num = intCheck()
    print("La somme des chiffres positifs saisis est :", sum)

#exo3()

## 4. Modifier ce dernier algorithme pour afficher la moyenne de la série d’entiers positifs saisis.
def exo4():
    sum = 0
    num = intCheck()
    i=0
    while num >= 0:
        sum = sum + num
        i+=1
        num = intCheck()
    print("La moyenne des chiffres positifs saisis est :", sum/i)

exo4()