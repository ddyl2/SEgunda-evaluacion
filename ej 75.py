 #Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por 
#pantalla los siguientes resultados:
#a. Cantidad total de valores
#b. Cantidad de números
#c. Cantidad de letras
#d. Cantidad de mayúsculas
#e. Suma de los valores numéricos
Lista1=['a','b','D','x','r','X','3','h','w','2','i']

total=len(Lista1)

total_num=0
for valor in Lista1:
    if valor.isdigit():
        total_num+=1

total_letras=0
for valor in Lista1:
    if valor.isalpha():
        total_letras+=1

total_mayus=0
for valor in Lista1:
    if valor.isupper():
        total_mayus+=1

suma_num=0
for valor in Lista1:
    if valor.isdigit():
        suma_num+=int(valor)

print("numero de valores",total)
print("cantidad de numeros",total_num)
print("cantidadde leras",total_letras)
print("cantidad de mayusculas",total_mayus)
print("suma total de numeros",suma_num)
