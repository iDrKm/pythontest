import time

CantDetergente=17
if CantDetergente>=5:
    cantRopa=int(input("cuantos kg de ropa de color tiene: "))
    if cantRopa>=5:
        CantDetergente-3
        print("la cantidad de detergente es ", CantDetergente)
        print("comineza ciclo de lavado")
        print("lavando")
        time.sleep(1)
        print("lavando")
        time.sleep(1)
        print("Sigue lavando")
        time.sleep(1)
        print("Ropa lista para secar")
    else:
        print("No tiene ropa de color suficiente")    
else:
    print("no tiene suficiente detergente")



if CantDetergente>=4:
    cantRopa=int(input("cuantos kg de ropa blanca tiene:  "))
    if cantRopa>=5:
        CantDetergente-4
        print("la cantidad de detergente es ", CantDetergente)
        print("comineza ciclo de lavado")
        print("lavando")
        time.sleep(1)
        print("lavando")
        time.sleep(1)
        print("Sigue lavando")
        time.sleep(1)
        print("Ropa lista para secar")
    else:
        print("No tiene ropa de color suficiente")  
else:
    print("no tiene suficiente detergente")


