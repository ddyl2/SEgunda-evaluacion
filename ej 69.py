lisnum = []
contador = 0
veces = int(input("¿Cuantas veces deseas repetir?: "))
while(contador != veces):
    numero = int(input("Introduce un numero: "))
    lisnum.append(numero)
    lisnum.sort()
    contador = contador + 1
print(lisnum)