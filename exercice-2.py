# -*- coding: utf-8 -*- 
# Exercice sur les formulaires
from tkinter import *

# Nouveau formulaire
maFenetre = Tk()

# Attributs de l'objet fenetre
maFenetre.title("Intégration du cadastre")
maFenetre.geometry("400x300")

# label
monLabel = Label(maFenetre, text="Choisir une commune")
monLabel.pack()
# Init liste (code_insee,"code_insee - nom_commune")
maListeCommune = Listbox(maFenetre,width='100')
maListeCommune.insert(85001,"85001 - L'AIGUILLON-SUR-MER")
maListeCommune.insert(85002,"85002 - L'AIGUILLON-SUR-VIE")
maListeCommune.insert(85003,"85003 - AIZENAY")
maListeCommune.insert(85004,"85004 - ANGLES")
maListeCommune.insert(85005,"85005 - ANTIGNY")
maListeCommune.insert(85006,"85006 - APREMONT")
maListeCommune.pack()

# bouton
bouton=Button(maFenetre, text="Intégrer")
bouton.pack()

# afficher
maFenetre.mainloop()