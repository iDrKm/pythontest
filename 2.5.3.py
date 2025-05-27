# 2.5.3
import time 




def pago():
    print("Portal de pagos")
    deuda=100000
    while True:
        print(f"Su deuda actual es de {deuda} ")
        opcion=int(input("""
                         Escoga opcion
                         1-Pagar deuda
                         2-Revirar deuda
                         3-salir
                         """))
        match opcion:
            case 1:
                pagar=int(input("ingrese el monto que desea pagar"))
                print(f"usted pago {pagar}")
                deuda=deuda-pagar
                time.sleep(1)
                print("pagado")
            case 2:
                print(f"Su deuda actual es de {deuda} ")
            case 3:
                print("Saliendo")
                break





def compra():
    print("Menu de compra")
    while True:
        while True:
            
            plata=int(input("Ingrese el monto de la compra "))
            deuda=deuda+plata
            time.sleep(1)
            print("compra realizada")
            return
    




def menu():
    while True:
        while True:
            try:
                print("Bienvenido a su banco")
                op=int(input("""
                            Seleccione una opcion
                            1-Pagar tarjeta
                            2-Realizar compra
                            3-Salir
                            """))
                break
            except Exception:
                print("Solo numeron enteros")
        match op:
                case 1:
                    print("Abriendo portal de pago")
                    time.sleep(1)
                    pago()
                case 2:
                    print("Abriendo menu de compra")
                    time.sleep(1)
                    compra()
                case 3:
                    print("saliendo")
                    break
                case _:
                    print("Opcion invalida")
 
menu()