
num=0
num2=0
var1=0
var2=0

valores=input()


if valores!=ValueError:
    partes=valores.split()
    var1=partes[0]
    var2=partes[1]
    op=int(var1)+int(var2)
    print(op)
if valores==IndexError:
    var1=input()
    var2=input()
    op=int(var1)+int(var2)
        
    
    print(op)
