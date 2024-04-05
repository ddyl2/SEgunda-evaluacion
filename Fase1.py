import random
Lista_palabrasecreta=[ "gato","arbol","montaña","pelota","ordenador","perro","agua","gas","pajaro","matematicas"]
lisrep=[]
Lista_partida=[]
Lista_ahorcado=[]
letra=""
longitud=0
rep=0
num2=0

var1=["","A","H","O","R","C","A","D","O"]
num=0
num2=0


secreta=random.randint(0,1)
secreta=Lista_palabrasecreta[secreta]
print(secreta)
longitud=len(secreta)
for cont in range(longitud):
    rep=( "_")
    Lista_partida.append( rep)
print(Lista_partida)


while longitud!=num2 and num!=8:
        posi=-1
        fallo=0
        acierto=0

        letra=input("introduce una letra: ")
        lisrep.remove
        
        for recorrido in secreta:
            posi+=1
            if letra!=lisrep:
                if recorrido==letra:
                    
                    Lista_partida[posi]=letra
                    acierto+=1
                    num2+=1
            
                
        lisrep.append(letra)
            
                
        print(Lista_partida)
            
        if acierto==0:
            fallo+=1
    


        if fallo==1:
                num+=1
                Lista_ahorcado.append(var1[num])
                print(Lista_ahorcado)

if num2==longitud:
    print("HAS GANADO")
