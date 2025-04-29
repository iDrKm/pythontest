
#4 Ingresar un número positivo, multiplicarlo por 5, restarle 8, 
# sumarle 3 y dividirlo por 2   

num=-1
while num <0:
    num=int(input("ingrese numero: "))
    if num<0:
        print("ingreso un valor negativo! vuelva a intentar")
total=num*5
total=total-8
total =total +3        
total /=2
print(f"el valor final es {total}")