def print_head(text_head, width=44):
    """Imprime el encabezado de cada menú"""
    
    left = int((width-len(text_head))/2)
    right = width - 2 - len(text_head) - left
    print("┌" + "─" * (width-2) + "┐")
    print("│" + " " * left + text_head + " " * right + "│")
    print("└" + "─" * (width-2) + "┘")
def mostrar_notas():
    print_head("Notas")
    for i in range(len(notas)):
        print(i+1, ".-", notas[i]) 



import os
notas=[7, 4.0, 2.3, 6, 7, 5.2, 3.8, 4]
while True:
    print_head("Menu de notas")
    print("""
          1.-Ingresar nota
          2.-Borrar nota
          3.-Mostrar notas
          4.-Sacar promedio, nota mayor y nota menor
          5.-limpear notas 
          6.-Salir
          """)
    op=int(input("Selecciones una opcion: "))
    os.system("cls")
    match op:
        case 1:
            nom=input("ingrese una nota: ")
            notas.append(nom)
            print(notas)
        case 2:
            mostrar_notas()
            rm=int(input("Ingrese el numero de la nota que desea borrar"))
            notas.pop(rm-1)
        case 3:
            mostrar_notas()
        case 4:
            if len(notas)==0:
                print()
            else:
                promedio=sum(notas)/len(notas)
            print(f"el promedio de notas es: {round(promedio, 1)}")
            print(f"la nota mas alta es: {max(notas)}")
            print(f"la nota mas baja es: {min(notas)}")
        case 4:
            # cont=0
            # for n in notas:
            #     print(cont, ".-", notas[cont], "  ", apellidos[cont])
            #     cont+=1  
            for i in range(len(notas)):
                print(i+1, ".-", notas[i])  
        case 6:
            print("Saliendo")
            break
        case _:
            print("Ingrese una opcion valida")


