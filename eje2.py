#2 Pida al usuario ingresar números, al final debe mostrar cuántos números
#  se ingresaron y mostrar la suma de todos ellos, para terminar, debe poner
#  la palabra salir


cont=0
total=0
opc=0
while opc!=2:
    print("1.- Ingresa nuevo numero")
    print("2-. salir")
    opc=int(input())
    if opc==1:
        a=int(input("ingreseel numero que desea: "))
        cont+=1
        total+=a
print(f"la cantidad de numeros ingresados son : {cont} ")
print(f"la suma es : {total}")