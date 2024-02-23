#Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida),
# en esta lista no deben almacenarse las letras que se han introducido repetidas.

letras=[]
respuesta="s"

respuesta=input("quieres comenzar? s/n: ")
while respuesta=="s":
    letra=input("introduce una letra: ")
    while letra.isnumeric() :
        letra=input("introduce una letra: ")
    
    if letra not in letras:
        letras.append(letra)
            
    
    
    respuesta=input("deseas continuar s/n: ")
else:
    print(letras)

