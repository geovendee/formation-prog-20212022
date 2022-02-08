# -*- coding: utf-8 -*- 

## Exercie final : Intégration du cadastre

# Import module
import urllib.request
import zipfile
import os
from tkinter import *

# Nouveau formulaire
fenetre = Tk()

# Attributs de l'objet fenetre
fenetre.title("Intégration du cadastre")
fenetre.geometry("500x300")

# Init label
label = Label(fenetre, text="Choisir une commune")
label.pack()

# Init liste (code_insee,"code_insee - nom_commune")
liste = Listbox(fenetre,width=100)
liste.insert(1,"85001 - L'AIGUILLON-SUR-MER")
liste.insert(2,"85002 - L'AIGUILLON-SUR-VIE")
liste.insert(3,"85003 - AIZENAY")
liste.insert(4,"85004 - ANGLES")
liste.insert(5,"85005 - ANTIGNY")
liste.insert(6,"85006 - APREMONT")
liste.pack()

####################################
## Recupérer la commune sélectionnée
####################################
def getCommuneSelected():
    if len(liste.curselection()) > 0:
        
        # Afficher la selection courante
        print(liste.get(liste.curselection()))
        print(liste.get(liste.curselection())[0:5])
        
        # URL du cadastre à telecharger (téléchargement à la commune)
        url = r"https://cadastre.data.gouv.fr/bundler/cadastre-etalab/communes/" + liste.get(liste.curselection())[0:5] + "/shp/parcelles"
        
        # créer le repertoire de destination "cadastre-etalab' si il n'existe pas
        print(os.path.exists(r"C:\FORMATION\Cours_Programmation_20212022\cadastre-etalab"))
        if os.path.exists(r"C:\FORMATION\Cours_Programmation_20212022\cadastre-etalab") == False :
            os.mkdir(r"C:\FORMATION\Cours_Programmation_20212022\cadastre-etalab")
        
        # Destination où recuperer le zip
        dest = r'C:\FORMATION\Cours_Programmation_20212022\cadastre-etalab\cadastre_'+liste.get(liste.curselection())[0:5]+'.zip'
        
        # Téléchargement du fichier
        # python3
        urllib.request.urlretrieve(url,dest) 
        # python2
        # urllib.urlretrieve(url,dest)
        
        # Message information
        print ("Fichier cadastre de la commune "+ liste.get(liste.curselection()) +" téléchargé avec succès")        
        
        # Décompresser le fichier
        fzip = zipfile.ZipFile(dest, 'r')
        fzip.extractall(r"C:\FORMATION\Cours_Programmation_20212022\cadastre-etalab")
        fzip.close()
        
        # Message information
        print ("Fichier cadastre de la commune "+ liste.get(liste.curselection()) +" decompressé avec succès")
    
        # Executer le .BAT
        try:
            os.system(r"C:\FORMATION\Cours_Programmation_20212022\cmd_ogr2ogr.bat")
        except:
            print ("Erreur rencontrée lors de l'execution du fichier .bat")
    
    else:
        print("Aucune sélection trouvée")

# Init bouton
bouton=Button(fenetre, text="Intégrer", command= getCommuneSelected)
bouton.pack()

# Afficher la fenêtre
fenetre.mainloop()