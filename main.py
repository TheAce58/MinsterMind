#Titel :        MinsterMind
#Librairy :     Turtle
#Date :         25.01.2021
#Author :       Thomas Stäheli

#Descript :     Jeu Minstermind en interface turtel avec 5 couleurs à dispositions afin de trouver
#               la bonne combinaison de 4 couleurs

#last modif:    29.01.2021

#A ameliorer : Effacer en cas d'erreur, aléatoire de la réponse pas + de 2 fois la même couleur
from turtle import *
from time import *
from random import *

#variable

noir = 0
blanc = 0
loose = 10
x = 0
case = 0
axeXC = -465
axeXR = 195
axeY = 430
entree = [0, 0, 0, 0]
fcase = [0, 0, 0, 0]
freponse = [0, 0, 0, 0]
tabreponse = [0, 0, 0, 0]
frandint = [0, 0, 0, 0, 0, 0]
aleatoire = 1
style = ('Arial', 100, 'bold')

#dictionnaire

couleurinterface = {
    'contour' : '#424242',
    'fond' : '#8C8C8C',
}

couleurs = {
    'red' : "rouge",
    'yellow' : 'jaune',
    'blue' : 'blue',
    'green' : 'vert',
    'orange' : 'orange'
}

numerocouleur = {
    1 : 'red',
    2 : 'yellow',
    3 : 'blue',
    4 : 'green',
    5 : 'orange',
}

lettrecouleur = {
    'r' : 'red',
    'j' : 'yellow',
    'b' : 'blue',
    'v' : 'green',
    'o' : 'orange'
}

lettrenumerocouleur = {
    'r' : 1,
    'j' : 2,
    'b' : 3,
    'v' : 4,
    'o' : 5
}

#fonction
def interface(axeXC, axeY):
    goto(axeXC, axeY)
    for i in range(10):
        for j in range(4):
            color(couleurinterface['contour'])
            dot(80)
            color(couleurinterface['fond'])
            dot(70)
            forward(35)
            pencolor(couleurinterface['contour'])
            forward(5)
            pencolor('purple')
            forward(60)
        axeY -= 95
        sety(axeY)
        setx(axeXC)


def afficheReponse(axeXC, axeY):
    goto(axeXC, axeY)
    for y in range(1):
        for x in range(4):
            color(numerocouleur[tabreponse[x]])
            dot(70)
            pencolor(numerocouleur[tabreponse[x]])
            forward(35)
            pencolor('purple')
            forward(55)
        sety(axeY - 90)
    sety(340)

def reponse():
    i = 1
    check = 0
    stay = 1
    while True:
        for x in range(4):
            tabreponse[x] = randint(1, 5)

        #si le code couleur possède plus de deux fois la même couleur
        if(tabreponse[0] == tabreponse[1]):
            if(tabreponse[0] == tabreponse[2] or tabreponse[0] == tabreponse[3]):
                stay = 1
        else:
            if(tabreponse[0] == tabreponse[2] and tabreponse[0] == tabreponse[3]):
                stay = 1
            else:
                if(tabreponse[1] == tabreponse[2] and tabreponse[1] == tabreponse[3]):
                    stay = 1
                else:
                    stay = 0
        if(stay == 0):
            break

def couleuraleatoire(aleatoire):
    aleatoire += 1
    sleep(0.05)
    if (aleatoire == 5):
        aleatoire = 1
    return aleatoire
#main

#Screen

ecran = Screen()
ecran.setup(1100, 1000)
ecran.bgcolor("purple")
pencolor('purple')
hideturtle() #cache la tortue

speed(0)
reponse()

interface(axeXC, axeY)

print("Bienvenue dans le MinsterMind !")
#afficheReponse(axeXC, axeY)

setx(-525)
sety(axeY)
forward(20)
pencolor(couleurinterface['contour'])
forward(5)
pencolor(couleurinterface['fond'])
setx(axeXC)

while True:

    #entrées des couleurs
    print("Choisissez un code de 4 couleurs : 'r' = rouge 'j' = jaune 'b' = bleu 'v' = vert 'o' = orange : ")
    for j in range(4):
        while True:
            entree[j] = input()
            if(entree[j] == 'r' or entree[j] == 'j' or entree[j] == 'v' or entree[j] == 'b' or entree[j] == 'o'):
                break
            else:
                print("Error : Veuillez sélectionner à nouveau pour la case", j + 1)
        dot(70, lettrecouleur[entree[j]])
        pencolor(lettrecouleur[entree[j]])
        forward(35)
        pencolor(couleurinterface['contour'])
        forward(5)
        pencolor('purple')
        forward(20)
        pencolor(couleurinterface['contour'])
        forward(5)
        if(j == 3):
            pencolor('purple')
        else:
            pencolor(couleurinterface['fond'])
        forward(35)

    #Regarde les réponses données

    #Regarde bien placé + bonne couleur
    for j in range(4):
        if(tabreponse[j] == lettrenumerocouleur[entree[j]]):
            fcase[j] = 1
            freponse[j] = 1
            noir += 1
        else:
            fcase[j] = 0
            freponse[j] = 0

    #Regarde bonne couleur + mal placé

    case = 1
    for i in range(3):
        if(lettrenumerocouleur[entree[0]] == tabreponse[case] and freponse[case] == 0 and fcase[0] == 0): #case 1, 2, 3
            blanc += 1
            fcase[0] = 1
            freponse[case] = 1
        else:
            case += 1

    case = 0
    for j in range(3):
        if(lettrenumerocouleur[entree[1]] == tabreponse[case] and freponse[case] == 0 and fcase[1] == 0): #case 0, 2, 3
            blanc += 1
            fcase[1] = 1
            freponse[case] = 1
        else:
            if(case == 0):
                case += 2
            else:
                case += 1

    case = 0
    for k in range(3):
        if(lettrenumerocouleur[entree[2]] == tabreponse[case] and freponse[case] == 0 and fcase[2] == 0): #case 0, 1, 3
            blanc += 1
            fcase[2] = 1
            freponse[case] = 1
        else:
            if(case == 1):
                case += 2
            else:
                case += 1

    case = 0
    for j in range(3):
        if(lettrenumerocouleur[entree[3]] == tabreponse[case] and freponse[case] == 0 and fcase[3] == 0): #case 0, 1, 2
            blanc += 1
            fcase[3] = 1
            freponse[case] = 1
        else:
            case += 1

    setx(axeXR)
    #Affiche le nombre de noir
    for i in range(noir):
        dot(70, 'black')
        pencolor('black')
        forward(35)
        pencolor('purple')
        forward(55)

    #Affiche le nombre de blanc
    for i in range(blanc):
        dot(70, 'white')
        pencolor('white')
        forward(35)
        pencolor('purple')
        forward(55)

    #enlève un essai (10 essais max)
    loose -= 1

    sleep(0.5)
    #victoire si les 4 couleurs sont placées correctement
    if(noir == 4):
        print("Bravo ! Vous avez trouvé la bonne réponse !!")
        print("Il vous restait", loose, "essais")
        clear()
        while True:
            goto(0, 0)
            aleatoire = couleuraleatoire(aleatoire)
            color(numerocouleur[aleatoire])
            write('YOU WIN', font=style, align='center')
    else:           #jeu continue
        noir = 0    #remise des réponses à 0
        blanc = 0
        for i in range(4):
            fcase[i] = 0    #flag remis à 0
            freponse[i] = 0

    #Défaite après 10 essais
    if(loose > 0):
        print("Il vous reste", loose, "essais")
        axeY -= 135
        sety(axeY)
        setx(axeXC)
        pencolor(couleurinterface['contour'])
        axeY += 5
        sety(axeY)
        pencolor(couleurinterface['fond'])
        axeY += 35
        sety(axeY)
    else:
        print("Dommage !!")
        print("La réponse était :")
        for i in range(4):
            print(couleurs[numerocouleur[tabreponse[i]]], " ", end='')
        clear()
        while True:
            goto(0, 0)
            aleatoire = couleuraleatoire(aleatoire)
            color(numerocouleur[aleatoire])
            write('YOU LOOSE', font=style, align='center')