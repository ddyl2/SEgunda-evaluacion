import time
import random
Lista_palabrasecreta=[ "gato","arbol","montaña","pelota","ordenador","perro","agua","gas","pajaro","matematicas"]
partida="s"
var1=""
numsecreta=10
contador=0


var1=input("quieres añadir una nueva palabra? s/n: ")

if var1=="s":
    
    veces=int(input("cuantas quieres añadir?: "))
    for cont in range(veces):
        numsecreta+=1
        nueva=input("introduce la nueva palabra: ")
        Lista_palabrasecreta.append(nueva)

while partida =="s":

    lisrep=[""]
    Lista_aciertos=[]
    Lista_errores=[]
    Lista_partida=[]
    Lista_ahorcado=[]
    letra=""
    longitud=0
    rep=0
    num2=0
    partida="s"

    var1=["","A","H","O","R","C","A","D","O"]
    num=0
    num2=0
    inicio=time.time()
    secreta=random.randint(0,numsecreta)

    secreta=Lista_palabrasecreta[secreta]
 
    Lista_palabrasecreta.remove(secreta)
    longitud=len(secreta)
    print(secreta)
    for cont in range(longitud):
        rep=( "_")
        Lista_partida.append( rep)
    print(Lista_partida)
    


    while longitud!=num2 and num!=8:
            posi=-1
            fallo=0
            acierto=0

            letra=input("introduce una letra: ")
            lisrep.append(letra)
            
            
            for recorrido in secreta:
                posi+=1
                if letra!=lisrep[0]:
                
                    if recorrido==letra:
                        
                        Lista_partida[posi]=letra
                        acierto+=1
                        Lista_aciertos.append(letra)
                        num2+=1
                if letra==lisrep[0]:
                      letra=input("vuelve a introducir otra letra:  ")
            lisrep.pop(0) 
                         
                
                
                    
            print(Lista_partida)
                
            if acierto==0:
                fallo+=1
        


            if fallo==1:
                    Lista_errores.append(letra)
                    num+=1
                    Lista_ahorcado.append(var1[num])
                    print(Lista_ahorcado)

    if num2==longitud:
        print("HAS GANADO")
    final=time.time()
    tiempo=(final-inicio)
    tif=round(tiempo,2)
    resumen1=len(Lista_aciertos)
    resumen2=len(Lista_errores)
    print(resumen1,"aciertos")
    print(tif,"s")
    print(resumen2,"fallos")

    partida=input("quieres repetir? s/n: ")

x=open('Text.txt', 'w+')
x.write(resumen1,"\n")
    