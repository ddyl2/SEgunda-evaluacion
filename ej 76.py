#A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras 
#y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás 
#en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.
Lista1=['a','b','D','x','r','X','3','h','w','2','i']

letras=[valor for valor in Lista1 if valor.isalpha()]
num=[valor for valor in Lista1 if valor.isnumeric()]

orden=int(input("introduce un 1 para ascendente o 2 para ascendente"))
if 1== orden:
    letras.sort()
    num.sort()
if 2== orden:
    letras.sort(reverse=True)
    num.sort(reverse=True)

print(num)
print(letras)