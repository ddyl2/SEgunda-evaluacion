#2. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al 
#azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine 
#la palabra


import random
respuesta=""
fin=1
lista=['casa','barco','gato','perro','madera','agua','puente','pantalón']
secreto=(random.choice(lista))
while secreto!=respuesta:
    respuesta=input("introduce una palabra:" )
    if respuesta==secreto:
        print("ACERTASTE")
        fin=1
    else:
        print("SIGUE JUGANDO")
        fin=2