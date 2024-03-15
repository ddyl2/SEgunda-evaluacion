
valores=str(input())
partes=valores.split()
var1=partes[0]
var2=partes[1]
var1=int(var1)
var2=int(var2)
enter, residu=divmod(var1,var2)
print(enter, residu)