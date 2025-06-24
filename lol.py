import os
def print_head(text_head, width=44):
    """Imprime el encabezado de cada menú"""
    
    left = int((width-len(text_head))/2)
    right = width - 2 - len(text_head) - left
    print("┌" + "─" * (width-2) + "┐")
    print("│" + " " * left + text_head + " " * right + "│")
    print("└" + "─" * (width-2) + "┘")

print_head("Menu de juegos")

juegos={
    1:{
        "nombre": "Metroid",
        "precio":50000,
        "code": "MMdd2023"
        },
    2:{
        "nombre": "Pikmin 4",
        "precio":55000,
        "code": "pKMn2022"
        }
}
# print(juegos[1])
# print(juegos[2])

# for j, datos in juegos.items():
#     print(j, datos)


def validar():
    print()

def mostrar_juegos(dic):
    for j, datos in dic.items():
                print(j, datos)

def act_juegos(dic):
     print()

while True :
    try:    
        print_head("Elija una opcion")
        op=int(input('''Ingrese una opcion
                1.-Agregar Juego
                2.-Mostrar juego
                3.-Actualizar juego
                4.-Borrar juego
                5.-Salir
                '''))
    except ValueError as e:
          print("ERROR") 
    match op:
        case 1:
            nombre=input("Ingrese el nombre del juego: ")
            precio=int(input("Ingrese el precio: "))
            code=input("Ingrese el codigo: ")
            
            largo=len(juegos)
            juegos[largo+1]={
                    "nombre": nombre,
                    "precio": precio,
                    "code": code,      
                    }
            
        case 2:
            mostrar_juegos(juegos)
        case 3:
            mostrar_juegos(juegos)


        case 4:
            mostrar_juegos(juegos)
            borrar=int(input("Cual juego desea borrar?: "))
            del juegos[borrar]            
        case 5:
            print("Saliendo")
            break
        case _: 
            print("Opcion invalida")
