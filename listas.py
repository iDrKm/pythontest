#uso y ejemplo de listas
#lista: coleccion de datos


#     -6 -5 -4 -3 -2 -1 
numeros=[3,22,7,21,84,2]
#      0 1  2  3  4 5


# print(numeros)

#print(lista.index(84))

# numeros.append(2)

# print(numeros)

# for numero in numeros:
#     print(f"nota: {numero*3}")

# num=int(input("ingrese un numero"))

# numeros.append(num)




nombres=["Hideo", "Mario", "Jhon" ]
apellidos=["Kojima", "Bros", "Kennedy"]
while True:
    print("""
          1.-Ingrese nombre
          2.-Buscar nombre 
          3.-Mostrar lista
          4.-Salir
          """)
    op=int(input("Selecciones una opcion: "))
    match op:
        case 1:
            nom=input("ingrese un nombre: ")
            nombres.append(nom)
            ape=input("ingrese un apellido: ")
            apellidos.append(ape)
            print(nombres)
            print(apellidos)
        case 2:
            busca=input("Ingrese nombre a buscar: ")
            if busca in nombres:
                print(f"El nombre {busca} existe en la lista")
            else:
                print(f"El nombre {busca} no existe en la lista")
        case 3:
            # cont=0
            # for n in nombres:
            #     print(cont, ".-", nombres[cont], "  ", apellidos[cont])
            #     cont+=1  
            for i in range(len(nombres)):
                print(i+1, ".-", nombres[i], apellidos[i])  
        case 4:
            print("Saliendo")
            break
        case _:
            print("Ingrese una opcion valida")




