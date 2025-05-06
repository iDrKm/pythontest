# calcular el puntaje de credito
# debe de calcular que atnto credito tiene una persona en cierta entidad financiera , debera considerar 
# cantidad de ingresos , nivel educacional y nacionalidad
# cantidad de ingresos 
# 500.000 a 1.000.000 : 300.000
# 1.000.000 a 1.500.000 : 650.000
# 1.500.001 o mas :1.000.000
# nivel educacional
# basico :x1, medio:x1,3 , superior: x1.5 
# nacionalidad
# chilena +300.000, extrangero : +0

credito=0
ingresos=int(input("ingresar la cantidad de sus ingresos"))
if ingresos>=500000:
    if ingresos>=500000 and ingresos<=1000000:
        credito=credito+300000
    elif ingresos>=1000001 and ingresos<=1500000:
        credito=credito+650000
    else:
        credito=credito+1000000

    educacion=int(input(""" 
                 Indique su nivel educacional
                 1.-Basico
                 2.-Medio
                 3.-Superior
                   """))
    if educacion==1:
        credito*=1
    elif educacion==2:
        credito*=1.3
    elif educacion==3:
        credito*=1.5
    else:
        print("Error, selecciono mal")

    nacionalidad=int(input("""
                   Indique su nivel educacional
                   1.-Chilena
                   2.-Extrangera
                   """))
    if nacionalidad==1:
        credito=credito+300000
    else:
        print("no aplica a nada ")


    
    print("Usted puede optar a un credito de: $", credito)


else:
    print("no aplica a credito")   
    
