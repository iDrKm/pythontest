def suma():
    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese otro numero"))
    print("El resultado es  ", n1+n2)
def resta():
    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese otro numero"))
    print("El resultado es  ", n1-n2)
def multi():
    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese otro numero"))
    print("El resultado es  ", n1*n2)
def division():
    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese otro numero"))
    try:
        print("El resultado es  ", n1/n2)
    except ZeroDivisionError:
        print("El resultado es indefinido")




    
    
def calcu():
    while True :
        try: 
            op=int(input('''Ingrese una opcion
                        1.-Suma
                        2.-Resta
                        3.-Multiplicacion
                        4.-Division
                        5.-Saliendo
                        '''))

            match op:
                case 1:
                    print("Suma")
                    suma()
                case 2:
                    print("Resta")
                    resta()
                case 3:
                    print("Multiplicacion ")
                    multi()
                case 4:
                    print("Division")
                    division()
                case 5:
                    print("Saliendo")
                    break

                case _: 
                    print("Opcion invalida")
        except ValueError as errorxd:
            print("Solo puede Ingresar numeros, no caracteres")
            print("error:", errorxd)    
calcu()
