from random import choice
from unidecode import unidecode


tentative = 6

#tirage de mot au hasard
def word():
    f = open('mot5.txt', 'r', encoding='utf8')
    contenu = f.readlines()
    return unidecode(choice(contenu)).upper().replace('\n', '')


# une fonction qui rend les espaces pour la place de lettre du mot

def underscore(mot, L=[]):
    r = ''
    for i in mot:
        if i in L:
            r += i + ' '
        else:
            r += '_ '

    return r[:-1]


# saisie  des lettre du mot a trouver

def saisie():
    lettre = input('Entrez une lettre : ')
    if len(lettre) != 1 or ord(lettre) < 65 or ord(lettre) > 122:
        return saisie()
    else:
        return lettre.upper()


# programme principal du projet
# ie execution des fontions deja creer

lettres_deja_proposees = []
print("vous avez 6 tentative \n et 3 point_erreur")
mot_a_deviner = word()
affichage = underscore(mot_a_deviner)
print('Mot à deviner : ', affichage)
nb_erreurs = 0

while '_' in affichage and nb_erreurs < 6:
    lettre = saisie()
    if lettre not in lettres_deja_proposees:
        lettres_deja_proposees += [lettre]
    if lettre not in mot_a_deviner:
        nb_erreurs += 1
        if nb_erreurs >=6:
            print('vous avez perdu')
            print(" +----+")
            print(" |    |")
            print(" |    o")
            print(" |   /|\\")
            print(" |    |")
            print(" |   / \\")
            print(" | ")
            print("_|_")
            print("| |")
            print("le mot s\'etait:", mot_a_deviner, '\n')

            break
    if affichage is mot_a_deviner:
        print("bravo! vous avez gagner")
        print("le score est:", score)

    affichage = underscore(mot_a_deviner, lettres_deja_proposees)
    print('\nMot à deviner : ', affichage, ' ' * 50, ' maximum de tentative est de :', 6 - nb_erreurs,'\n')
    score =(6-nb_erreurs)*len(mot_a_deviner)
