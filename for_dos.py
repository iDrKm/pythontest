#Perros de caza, pida al usuario la cantidad de perros 
# muestre cual es la cuota minima de conejos 
# luego consulte cuantos conejos trajo la cantidad minima 
# cumplio la cuota , sino se queda sin Filete 
# mostrar resumen de perros que cumplieron y los que no
import random
from random import randint
import time
perros=0
conejos=4
perros_si=0

print(f"la cuota de conejos es {conejos}")

while perros==0:
    perros=int(input("cantidad de perros? "))
    try:
        if perros <0:
            print("ingrese valores arriba de 0")
    except ValueError:
        print("ingrese valores de numeros enteros")
        
for i in range (perros):
    time.sleep (1)
    conejos_atrapados=random.randint(0,8)
    if conejos_atrapados>=conejos:
        print(f"El perro numero {i+1} atrapo {conejos_atrapados} conejos " )
        print(f"El perro cumple con la cuota" )
        print("-----------------------------------------")
        perros_si=perros_si+1
    else:
        print(f"Perro numero {i+1} trajo {conejos_atrapados} conejos")
        print(f"Perro numero no cumple la cuota, se queda in filete")
        print("--------------------------------------")

print(f"Los perros que cumplen la cuota son {perros_si}")
print(f"Los perros que no cumplieron la cuota fue {perros_si-perros}")











