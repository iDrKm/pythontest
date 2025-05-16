#crear un menu de carritocon las siguientes opciones
#1-ingresar nombre del usuario
#sera mostrando en la boleta, con un saludo 
#2- comprar , poner productos para poder comprar con su precio correspondiente 
#3- sacar boleta , calcular precio neto y el precio mas iva . mostrando totales
#bonus contar la cantidad de articulos 
#4 salir
#consideraciones :
#or lo menos 3 productos 
#no hay limite de compra
#Se puede salir en cualquier momento 
#

def usuario():
    usuario1=(input("Ingrese su usuario: "))
    return usuario1

def comprar():
    total=0
    cant=int(input("Cunatos productos llevara?  "))
    for i in range(cant):
        print("""
        "Que producto llevará?"
        "1.- Monster $1800"
        "2.- comida para gatos $13500"
        "3.- Papas frita  $1000"
        "4.- Paloma saltada  $8000"
              
        """)
        op=int(input())

        if op==1:
            print("usted lleva Monster")
            print("valor 1800")
            total=total+1800
        elif op==2:
            print("usted lleva comida para gatos")
            print("valor 13500")
            total=total+13500
        elif op==3:
            print("usted lleva papas frita")
            print("valor 1000")
            total=total+1000
        elif op==4:
            print("usted lleva paloma saltada")
            print("valor 8000")
            total=total+8000
        else:
            print("opcion no valida ")  
    return total
               


def boleta(total):

    print("el total neto es ", total) 
    print("el total mas iva es ", total*1.19)   




 
def opciones():
    while True :
        try: 
            op=int(input('''Ingrese una opcion
                        1.-Ingresar usuario
                        2.-Comprar
                        3.-Sacar boleta
                        4.-Salir
                        '''))

            match op:
                case 1:
                    nombre_usuario = usuario()
                    print(f"Hola {nombre_usuario} ")
                case 2:
                    totalx=comprar()
                case 3:
                    boleta(totalx)
                case 4:
                    print("Saliendo")
                    break
                case _: 
                    print("Opcion invalida")
        except ValueError as errorxd:
            print("Solo puede Ingresar numeros, no caracteres")
            print("error:", errorxd)    
opciones()