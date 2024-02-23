#A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y 
#no deben almacenarse en la lista
letras=[]
respuesta="s"

respuesta=input("quieres comenzar? s/n: ")
while respuesta=="s":
    letra=input("introduce una letra: ")
    while letra.isnumeric() :
        letra=input("introduce una letra: ")
    if letra not in ['á','é','í','ó','ú','à','è','ì','ò','ù']:
        if letra not in letras:
            letras.append(letra)
            
    
    
    respuesta=input("deseas continuar s/n: ")
else:
    print(letras)