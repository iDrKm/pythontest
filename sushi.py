# En un delivery de Sushi vende 4 tipos de Sushi:
# 1. Pikachu Roll $4500
# 2. Otaku Roll $5000
# 3. Pulpo Venenoso Roll $5200
# 4. Anguila Eléctrica Roll $4800

       

def sushi():
    boleta=0
    productos=0
    pika=0
    otakuroll=0
    pulpo=0
    anguila=0
    while True :
        boleta=0
        productos=0
        pika=0
        otakuroll=0
        pulpo=0
        anguila=0
        op=int(input('''Ingrese una opcion
                    1.-Pikachu Roll $4500
                    2.-Otaku Roll $5000
                    3.-Pulpo Venenoso Roll $5200
                    4.-Anguila Eléctrica Roll $4800
                    5.-Pedido completo, pasar a caja
                    '''))

        match op:
            case 1:
                print("Pikachu Roll $4500")
                boleta+=4500 
                productos=productos+1
                pika=pika+1
                
            case 2:
                print("Otaku Roll $5000")  
                boleta+=5000 
                productos=productos+1
                otakuroll=otakuroll+1
            case 3:
                print("Pulpo Venenoso Roll $5200 ") 
                boleta+=5200 
                productos=productos+1
                pulpo=pulpo+1
            case 4:
                print("Anguila Eléctrica Roll $4800")    
                boleta+=4800
                productos=productos+1
                anguila=anguila+1
          
            case 5:
                while True:
                    print("Posee codigo de descuento? 1.Si 2.No")
                    CodDscto=int(input())
                    if CodDscto==1:
                        while True:
                            cod=input(("Ingrese su codigo: "))
                            if cod=="soyotaku":
                                desc10=boleta*0.1
                                boleta=boleta-desc10
                                print("El total del descuento es $", desc10)
                                break
                            else:
                                print("codigo no valido o caducado")
                                nu=input(("Desea intentar nuevamente? 1-Si 2.No"))
                                if nu=="1":
                                    break


                    print("Opcion invalida") 
                    print(f"Total de productos {productos}")
                    print("--------------------")
                    print(f"Pikachu Roll  {pika}")
                    print(f"Otaku Roll {otakuroll}")
                    print(f"Pulpo Venenoso Roll {pulpo}")
                    print(f"Anguila Eléctrica Roll {anguila}")
                    print("--------------------")
                    print(f"Total de boleta {boleta}")
                    print(f"descuento por codigo {desc10}")

                       
                    
            case _:   
                ("codigo invalido")             

sushi()