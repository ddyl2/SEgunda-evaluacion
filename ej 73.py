#Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están 
#repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se 
#repiten y cuales no
lista1=['casa','mesa','sal','sol','agua']
lista2=['casa','luz','tres','tren','sol','pan']
repetidas=[]

for a in lista1:
    repetidas.append(a)
for a in lista2:
    repetidas.append(a)
if repetidas.count(lista1):
    repetidas.remove(lista2)
print(repetidas)