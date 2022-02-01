# -*- coding: utf-8 -*- 
# Exercie: les conditions / les boucles / Gestion des listes

import os

cheminFormation = "C:\\FORMATION"

# les fonctions + Les conditions
# --------------------------------
def testchemin(arg):
    if os.path.exists(arg):
        if os.path.isdir(arg):
            return "Le chemin est un répertoire."
        else:
            return "Le chemin est un fichier."
    else:
        return "Le chemin n'existe pas"

print("1er print : " + testchemin(cheminFormation) + " => " + cheminFormation)
print("2nd print : " + testchemin('cheminFormation'))
print("3ème print : " + testchemin(r'C:\FORMATION\nouveauRep\log.txt'))

# les boucles
# --------------------------------
maListe=os.listdir(cheminFormation)
print(maListe)
monFichier = open(cheminFormation + "\\nouveauRep\\listerep.txt","w")
for elementDeMaListe in maListe:
    monFichier.write(elementDeMaListe + "\n")
monFichier.close()

# Gestion des listes
# --------------------------------
v = [0,3,25,624]
print (v)
v.append(2365)
print(v)
for element in v:
    print(element)
# retourne l'élément pour l'index 4

print(v[4])
print("Dernier élément : " + str(v[4]))
                     
                     
        