# -*- coding: utf-8 -*-
import math
import os

# Question1 : aire d'un rectangle (longueur x largeur)
def rectangle(longueur,largeur):
    return (longueur*largeur)

print("Aire du rectangle : " + str(rectangle(25,5)))

# Question 2 : aire d'un cylindre (2 x π x rayon x hauteur)
def cylindre(rayon, hauteur):
    return (2*math.pi*rayon*hauteur)

print("Aire du cylindre : " + str(cylindre(8,12)))

# Question 3 : conversion en chiffre Romain
def convertChiffreRomain(i):
    out = ''
    
    if (i < 4):
        for x in range(i) :
            out = out + 'I'
    if (i == 4):
        out = 'IV'
    if (i == 5):
        out = 'V'
    if (i > 5 and i < 9) :
        out = 'V'
        for x in range(i-5) :
            out = out + 'I'
    if (i == 9):
        out = 'IX'
    if (i == 10):
        out = 'X'

    return out # retourne le chiffre Romain

print("3 en chiffre Romain : " + convertChiffreRomain(3))
print("4 en chiffre Romain : " + convertChiffreRomain(4))
print("7 en chiffre Romain : " + convertChiffreRomain(7))
print("9 en chiffre Romain : " + convertChiffreRomain(9))
print("10 en chiffre Romain : " + convertChiffreRomain(10))


# Question 4 : Générer un répertoire par commune (code INSEE)
communes_insee = [85001,85003,85004,85005]

def generateInseeDir(path):
    
    if (os.path.exists(path) == False):
        os.mkdir(path)
    
    for code_insee in communes_insee:
        if (os.path.exists(path+"\\"+str(code_insee)) == False):
            os.mkdir(path+"\\"+str(code_insee))
    return 'Création des répértoires par commune terminée'
            
print(generateInseeDir("C:\\FORMATION\\20210201"))

# Question 5 : Générer 50 répertoires (1-50)
def generateNumberDir(path):
    
    if (os.path.isdir(path) == False):
        os.mkdir(path)
    
    for x in range(1,51):
        if (os.path.exists(path+"\\"+str(x)) == False):
            os.mkdir(path+"\\"+str(x))
    return 'Création des 50 répertoires terminée'
            
print(generateNumberDir("C:\\FORMATION\\20210201"))

# Question 6 : liste des fichiers + taille ==> fichier texte
def readDir(path, outputFile):
    
    fw = open(outputFile, 'w')
    listdir = os.listdir(path)
    print(listdir)
    # Boucler sur les répertoires et fichiers
    for fileOrDirectory in listdir:
        if (os.path.isfile(path + "\\"+ fileOrDirectory)):
            fw.write(fileOrDirectory + " : " + str(os.path.getsize(path + "\\"+ fileOrDirectory)) + " octet")
            if (os.path.getsize(path + "\\"+ fileOrDirectory) > 0):
                fw.write("s")
            fw.write("\n")
    fw.close()

readDir('C:\\WINDOWS', 'C:\\FORMATION\\listerep.txt')