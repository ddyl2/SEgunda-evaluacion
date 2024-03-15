
valores=str(input())
partes=valores.split()
var1=partes[0]
var2=partes[1]
var2=int(var2)
var1=int(var1)

if (var1 <0) or (var2<0):
    if var1> var2:
        print(var1)
    if var1<var2:
        print(var2)
    if var1==var2:
        print(var1)
else:
    if var1<var2:
        print(var2)
    if var1>var2:
        print(var1)
    if var1==var2:
        print(var1)