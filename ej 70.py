lista1=[]
contador=0
palabras=int(input("introduce  numero de palabras: "))
while(contador != palabras):
    palabra=input("introduce una palabra: ")
    contador = contador + 1
    lista1.append(palabra)
lista2=lista1.copy()
lista2.sort(reverse = True)
print("Lista1 contiene :",lista1)
print("Lista2 contiene :",lista2)
