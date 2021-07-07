# -*-coding:Utf-8 -*

def auberge(age, pds):
    if age < 10:
        prix = 5
    elif age == 60:
        prix = 0
    else:
        if pds >= 20:
            prix = 40
        else:
            prix = 30

    print("Le prix pour votre chambre est", prix, "écus étant donné vos bagages ", pds, "kgs, et votre âge :", age, "ans.")

# auberge(x, y)

def fete(nb_pers, arr_dep):
    if int(len(arr_dep))/2 != int(nb_pers):
        print("Vous n'avez pas saisi les bonnes données : quelqu'un de non prévu est là ou alors ne repart pas.")
        quit()
    else:
        pres = 0
        members = []
        for ele in arr_dep:
            print("Actuellement présents :", pres, members)
            if ele > 0 and ele not in members:
                pres += 1
                members.append(ele)
            elif ele > 0 and ele in members:
                print("Etrange, cette personne est déjà là, votre liste d'arrivant doit être fausse")
                continue
            else:
                try:
                    members.remove(abs(ele))
                except ValueError:
                    print("Quelqu'un qui n'est pas là essaye de s'en aller")
                    continue
                pres -= 1

# fete(6, [1,3,-1,2,4,5,-2,-4,-5,6,-3, -6])

def disparu(num, tailleListe, liste_num):
    check = False
    for i in range(tailleListe):
        if liste_num[i] == num:
            print("Sorti de la ville")
            # Si on veut mettre fin au programme si oui : quit()
            check = True
        else:
            continue
    if check == False:
        print("Encore dans la ville")

#disparu(4, 11, [1,5,6,8,43,6,4,8,4,2,1])
#disparu(4, 11, [1,5,6,8,43,6,11,8,2,2,1])