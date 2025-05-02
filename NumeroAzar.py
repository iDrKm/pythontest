import random
numAdivinar=random.randint(1,50)

num=int(input("Adivine el numero: "))
while num!=numAdivinar:
   
    if num>numAdivinar:
        print("El numero es menor ")
    else:
        print("El numero es mayor")
    num=int(input("Adivie el numero "))
print("le achuntaste")