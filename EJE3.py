
#3 Pida al usuario ingresar un número y multiplícalo por un número al 
# azar entre 2 y 8. Si 
# el número es mayor que 50, logró la meta, si no, intente nuevamente

from random import randint
a=0
b=0
while a*b<50:
    a=int(input("ingrese el numero q desea: "))
    b=randint(2,8)
    print(f"valor generado:" , b)
    print(f"la multiplicacion {a}x{b}={a*b}")
print("logro la meta")
