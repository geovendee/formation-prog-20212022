# -*- coding: utf-8 -*- 
# Exercices sur les fonctions

## Exemple 1
def maFonctionAddition(arg1, arg2):
    # mes instructions
    value = arg1+ arg2
    # valeur retournée
    return value
print(maFonctionAddition(2,7))
print(maFonctionAddition(12,57))
print(maFonctionAddition(22,73))

# convertir les francs en euros
def franc2euro(vfranc):
    veuro = vfranc/6.55957
    return veuro

print(franc2euro(120))
print(franc2euro(20))

# suppression des accents
def suppaccent(texteaccentue):
    return texteaccentue.replace("é","e").replace("à","a").replace("è","e")

print(suppaccent("épàjhyè"))

print(maFonctionAddition(200,70))