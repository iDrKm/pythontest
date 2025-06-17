"""
realizar una funcion que calcule el iva 
realizar otra funcion que al pasarle el precio
y un numero cmo porcentaje (ej 20)
calcule el descuento y muestre el valor final
"""
def print_head(text_head, width=44):
    """Imprime el encabezado de cada menú"""
    
    left = int((width-len(text_head))/2)
    right = width - 2 - len(text_head) - left
    print("┌" + "─" * (width-2) + "┐")
    print("│" + " " * left + text_head + " " * right + "│")
    print("└" + "─" * (width-2) + "┘")



# def iva(n):
#     return n*0.19


# def dsct(precio, porc):
#     return precio*porc/100 

# neto=1500

# print("El iva es  ", iva(neto))
# print("Es precio total es ", dsct(neto)+neto)

productos=[
    {"nombre": "Lapiz", "precio":400},
    {"nombre": "Goma", "precio": 200},
    {"nombre": "Estuche", "precio": 1600},
]
# for producto in productos:
#     print("El precio del articulo ", producto["nombre"], " es ", producto["precio"])


while True :
        try:    
            print_head("Menuuuuu")
            op=int(input('''Ingrese una opcion
                    1.-Agregar Articulo
                    2.-Quitar Articulo
                    3.-Actualizar articulo
                    4.-Mostrar listado de articulos
                    5.-Saliendo
                    '''))
            match op:
                case 1:
                    nombre=input("ingrese el nombre del articulo: ")
                    precio=int(input("Ingrese el precio del nombre: "))
                    productos.insert(0,{"nombre":nombre, "precio":precio })
                case 2:
                    for producto in productos:
                         print(producto["nombre"], producto["precio"])
                    borrar=int(input("Seleccione cual desea borrar "))
                    productos.pop(borrar-1)
                    print("")
                case 3:
                    for n, producto in enumerate(productos):
                           print(n+1, producto["nombre"], producto["precio"])
                    act=int(input("Seleccione cual desea actualizar "))
                    precio=int(input("ingrese el nombre del precio"))
                    productos[act-1]["precio"] = precio
                case 4:
                      print(productos)              
                case 5:
                    print("Saliendo")
                    break
                case _: 
                    print("Opcion invalida")
        except ValueError as e:
            print("Error ")   