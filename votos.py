pikachu=0
dragonite=0

votantes=int(input("ingrese el numero de votantes "))
for i in range(votantes):
    print("""
    "Ingrese su voto 
    1. Pikachu 
    2. Dragonite  
     """)
    voto=int(input())
    if voto==1:
        print("voto para pikachu")
        pikachu=pikachu+1
    elif voto==2:
        print("voto para dragonite")
        dragonite=dragonite+1
    else:
        print("voto invalido seleccione una respuesta correcta")


print("los votos de pikachu son ", pikachu)
print("los votos de dragonite son ", dragonite)

if pikachu>dragonite:
    print("gano pikachu")
elif pikachu<dragonite:
    print("gano dragonite")
else:
    print("Empate")
    
