# -*- coding: utf-8 -*- 
# Manipulation des fichiers

# importer le module os permettant la manipulation de dossiers et fichiers
import os

# tester la présence d'un fichier et/ou repertoire
exist = os.path.exists("C:\\FORMATION")
print(exist)

# tester si le chemin est un fichier ou un répertoire
print("Est un fichier : " + str(os.path.isfile("C:\\FORMATION")))
print("Est un dossier : " + str(os.path.isdir("C:\\FORMATION")))

# lister le contenu du répertoire
print(os.listdir("C:\\FORMATION"))

# créer un répertoire
if os.path.exists("C:\\FORMATION\\nouveauRep") == False :
    os.mkdir(r"C:\FORMATION\nouveauRep")
print(os.listdir("C:\\FORMATION"))

# créer un fichier log.txt
fw = open(r"C:\FORMATION\nouveauRep\log.txt","w")

# intégrer la valeur "Bonjour tout le monde"
fw.write("Bonjour tout le monde\n")
fw.write("Au revoir")
fw.close()

# lire le contenu d'un fichier
fr = open(r"C:\FORMATION\nouveauRep\log.txt","r")
print(fr.read())