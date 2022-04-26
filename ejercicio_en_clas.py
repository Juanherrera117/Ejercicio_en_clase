"""PROGRAMA DE NUMERO PAR O IMPAR"""

print("----------------------------")
print("-------PAR O IMPAR----------")
print("----------------------------")

# input
X = input("Digite el valor de X: ")
X = int (X)
R = X%2 

# procesing
if R == 0 : 
    msj = "Par"
else :
    msj = "Impar"


# output
print( " El numero es " + msj)
