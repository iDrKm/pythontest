total=0
cant=int(input("Cunatos productos llevara?  "))
for i in range(cant):
    print("""
     "Que producto llevará?"
	 "1.- Diazepam $9000"
	 "2.- Metametozona $18500"
	 "3.- Oblea China $1000"
    """)
    op=int(input())

    if op==1:
        print("usted lleva Diazepam")
        print("valor 9000")
        total=total+9000
    elif op==2:
        print("usted lleva Metametazona")
        print("valor 18500")
        total=total+18500
    elif op==3:
        print("usted lleva oblea china")
        print("valor 1000")
        total=total+1000
    else:
        print("opcion no valida ")
print("el total neto es ", total) 
print("el total mas iva es ", total*1.19)        
