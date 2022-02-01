# -*- coding: utf-8 -*- 
# Exercices sur les variables
v1='bonjour'
print(v1)
v2=4
print(v2)
v3=10.25
print(v3)
v4 = ["un","deux","trois","quatre","cinq"]
print(v4)
v5 = v2+v3
print(v5)
v6='été'
print(v6)
v7="tout le monde"
print(v7)
# remplace texte
v6 = v6.replace("é","e")
print(v6)
# concatenation chaines
v8 = v1 + " " + v7
print(v8)
# nombre de caractère
print(len(v1))
# passage en majuscule
v7 = v7.upper()
print (v7)
# extraction chaine
v9 = v7[7:13]
print (v9)
# suppression espaces
v9 = v9.strip()
print (v9)
# decomposition chaine
v10 = v7.split(" ")
print (v10)