#calificar las personas segun su edad
#menor de 12 niño
#entre 12 y 17 es adolescente
#entre 18 y 64 adulto
# 65 y mas adulto mayor 


edad=int(input("Ingrese su edad: "))

if edad<12 :
    print("es un niño")
elif  edad>=12 and edad<=17:
    print("es adolescente")
elif edad>=18 and edad<=64 :
    print("es adulto")
else :
    print("es adulto mayor")
