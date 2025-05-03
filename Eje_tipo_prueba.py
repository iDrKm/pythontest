#EJERCICIO TIPO PRUEBA

import time
import random 
from random import randint
goles=randint(1,10)
print("Los goles anotados por el jugador esta temporada fueron: ", goles)
time.sleep(1)
pos=randint(1,16)
print("la posicion final en la temporada fue: ", pos)
time.sleep(1)
#goles=int(input("Cuantos goles anoto?  "))

sueldo=5000

if goles>=1 and goles<=3:
    sueldo=sueldo*1.04
elif goles>=4 and goles<=6:
    sueldo=sueldo*1.06
else:
    sueldo=sueldo*1.08
print("el sueldo aumentado es: ", sueldo)

if pos>=1 and pos<=3:
    sueldo+=3000
elif pos>=4 and pos<=6:
    sueldo+=2000
else:
    sueldo+1000

print("El total del sueldo del jugador al final de temporada es: ", sueldo)
