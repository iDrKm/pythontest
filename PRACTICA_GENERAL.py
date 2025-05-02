# total=0
# cant=int(input("Cunatos productos llevara?  "))
# for i in range(cant):
#     print("""
#      "Que producto llevará?"
# 	 "1.- Diazepam $9000"
# 	 "2.- Metametozona $18500"
# 	 "3.- Oblea China $1000"
#     """)
#     op=int(input())

#     if op==1:
#         print("usted lleva Diazepam")
#         print("valor 9000")
#         total=total+9000
#     elif op==2:
#         print("usted lleva Metametazona")
#         print("valor 18500")
#         total=total+18500
#     elif op==3:
#         print("usted lleva oblea china")
#         print("valor 1000")
#         total=total+1000
#     else:
#         print("opcion no valida ")
# print("el total neto es ", total) 
# print("el total mas iva es ", total*1.19)        

# ----------------------------------------------------------------------------------------------------------------------------


#  edad=int(input("Ingrese su edad: "))

# if edad<12 :
#     print("es un niño")
# elif  edad>=12 and edad<=17:
#     print("es adolescente")
# elif edad>=18 and edad<=64 :
#     print("es adulto")
# else :
#     print("es adulto mayor")


# _-------------------------------------------------------------------------------------

# n1=int(input("ingrese la nota 1: "))
# n2=int(input("ingrese la nota 2: "))
# n3=int(input("ingrese la nota 3: "))

# promedio=(n1+n2+n3)/3
# print("su promedio es ", round(promedio) )

# if promedio>=40 :
#     print("usted aprobo yiupiiii")
# else :
#     print("uste reprobo wuajaja")



# -------------------------------------------------------------------------------------------------------------------------


# import time

# CantDetergente=17
# if CantDetergente>=5:
#     cantRopa=int(input("cuantos kg de ropa de color tiene: "))
#     if cantRopa>=5:
#         CantDetergente-3
#         print("la cantidad de detergente es ", CantDetergente)
#         print("comineza ciclo de lavado")
#         print("lavando")
#         time.sleep(1)
#         print("lavando")
#         time.sleep(1)
#         print("Sigue lavando")
#         time.sleep(1)
#         print("Ropa lista para secar")
#     else:
#         print("No tiene ropa de color suficiente")    
# else:
#     print("no tiene suficiente detergente")



# if CantDetergente>=4:
#     cantRopa=int(input("cuantos kg de ropa blanca tiene:  "))
#     if cantRopa>=5:
#         CantDetergente-4
#         print("la cantidad de detergente es ", CantDetergente)
#         print("comineza ciclo de lavado")
#         print("lavando")
#         time.sleep(1)
#         print("lavando")
#         time.sleep(1)
#         print("Sigue lavando")
#         time.sleep(1)
#         print("Ropa lista para secar")
#     else:
#         print("No tiene ropa de color suficiente")  
# else:
#     print("no tiene suficiente detergente")

# ----------------------------------------------------------------------------------------------------

# uso y explicacion de while(mientras)
# num=0

# while num<=5:
#     print(num)
#     num+=1

# _________________________________________________________________________________________

# import time

# num=10

# while num>=0:
#     print(num)
#     time.sleep(1)
#     num-=1

# ___________________________________________________________________________



# resp="no"
# while resp!="si":
#     resp=input("Desea salir del sistema?  ")


# ---------------------------------------------------------------------

# clave=3344

# contraseña=int(input("Digite sua contraseña:  "))

# while clave!=contraseña:
#     print("Erro de chave inválida")
#     contraseña=int(input("Digite sua contraseña: "))
# print("Clave correcta")

# -------------------------------------------------------------------------------------------------

# pikachu=0
# dragonite=0

# votantes=int(input("ingrese el numero de votantes "))
# for i in range(votantes):
#     print("""
#     "Ingrese su voto 
#     1. Pikachu 
#     2. Dragonite  
#      """)
#     voto=int(input())
#     if voto==1:
#         print("voto para pikachu")
#         pikachu=pikachu+1
#     elif voto==2:
#         print("voto para dragonite")
#         dragonite=dragonite+1
#     else:
#         print("voto invalido seleccione una respuesta correcta")


# print("los votos de pikachu son ", pikachu)
# print("los votos de dragonite son ", dragonite)

# if pikachu>dragonite:
#     print("ganador pikachu")
# elif pikachu<dragonite:
#     print("ganador dragonite")
# else:
#     print("Empate")
    

# ----------------------------------------------------------------------------------

#EJERCICIO 1: CLASIFICAR NUMERO PAR IMPAR Y MOSTRAS LOS PARES E IMPARES HASTA EL NUMERO INGRESADO

# impar=0
# par=0
# n1=int(input("ingrese un numero:  "))
# if n1%2==0:
#      print(n1, " tu numero es par")
#      print("-------------------")
# else:
#     print(n1, " tu numero es impar")
#     print("-------------------")


# for i in range(1,n1+1):
#     if i%2==0:
        
#         print(i, " numero es par")
#     else:
       
#         print(i, " numero es impar")
        
#------------------------------------------------------------------------------------------------



#2 Pida al usuario ingresar números, al final debe mostrar cuántos números
#  se ingresaron y mostrar la suma de todos ellos, para terminar, debe poner
#  la palabra salir


# cont=0
# total=0
# opc=0
# while opc!=2:
#     print("1.- Ingresa nuevo numero")
#     print("2-. salir")
#     opc=int(input())
#     if opc==1:
#         a=int(input("ingreseel numero que desea: "))
#         cont+=1
#         total+=a
# print(f"la cantidad de numeros ingresados son : {cont} ")
# print(f"la suma es : {total}")

#---------------------------------------------------------------



#3 Pida al usuario ingresar un número y multiplícalo por un número al 
# azar entre 2 y 8. Si 
# el número es mayor que 50, logró la meta, si no, intente nuevamente

# from random import randint
# a=0
# b=0
# while a*b<50:
#     a=int(input("ingrese el numero q desea: "))
#     b=randint(2,8)
#     print(f"valor generado:" , b)
#     print(f"la multiplicacion {a}x{b}={a*b}")
# print("logro la meta")


#--------------------------------------------------------------------


#4 Ingresar un número positivo, multiplicarlo por 5, restarle 8, 
# sumarle 3 y dividirlo por 2   

# num=-1
# while num <0:
#     num=int(input("ingrese numero: "))
#     if num<0:
#         print("ingreso un valor negativo! vuelva a intentar")
# total=num*5
# total=total-8
# total =total +3        
# total /=2
# print(f"el valor final es {total}")

#-------------------------------------------------------------------------














