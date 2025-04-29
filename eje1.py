#EJERCICIO 1: CLASIFICAR NUMERO PAR IMPAR Y MOSTRAS LOS PARES E IMPARES HASTA EL NUMERO INGRESADO

impar=0
par=0
n1=int(input("ingrese un numero:  "))
if n1%2==0:
     print(n1, " tu numero es par")
     print("-------------------")
else:
    print(n1, " tu numero es impar")
    print("-------------------")


for i in range(1,n1+1):
    if i%2==0:
        
        print(i, " numero es par")
    else:
       
        print(i, " numero es impar")
        