#contar los autos que llegan al estacionamiento
#rojos azules y otros

rojos=0
azules=0
otro=0
color=0

while color!=4:

    color=int(input("""
                    Ingrese el colo del auto
                    1.- Rojo
                    2.- Azul
                    3.- Otro
                    4.-SALIR
                    """         ))
    if color==1:
        print("el color es rojo")
        rojos+=1
    elif color==2:
        print("el color es azul")
        azules+=1
    elif color==3:
        print("el color es otro")
        otro+=1
    else:
        print("saliendo")
print("los autos de color rojo son ", rojos)
print("los autos de color azul son ", azules)
print("los autos de otro color son ", otro)
    




























# Jugador=1000
# goles=0