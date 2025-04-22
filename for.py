# #explicacion de for 

# num=int(input("ingrese un numero"))

# for i in range(num) :
#     print(i)


# num=int(input("ingrese numero"))
# for i in range(10):
#     print(num, "x", i+1 , "=" , (i+1)*num)


cant=int(input("ingrese cant de notas "))
suma=0
for i in range(cant):
    print("ingrese la nota", i+1)
    nota=float(input())
    suma=suma+nota
prom=suma/cant
print("el promedio es:", prom)
