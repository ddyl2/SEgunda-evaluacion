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