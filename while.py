#uso y explicacion de while(mientras)
# num=0

# while num<=5:
#     print(num)
#     num+=1

#_________________________________________________________________________________________

# import time

# num=10

# while num>=0:
#     print(num)
#     time.sleep(1)
#     num-=1

#___________________________________________________________________________



# resp="no"
# while resp!="si":
#     resp=input("Desea salir del sistema?  ")


clave=3344

contraseña=int(input("Digite sua contraseña:  "))

while clave!=contraseña:
    print("Erro de chave inválida")
    contraseña=int(input("Digite sua contraseña: "))
print("Clave correcta")