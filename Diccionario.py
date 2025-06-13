dic={
    "nombre": "Jose Cornejo Espinoza",
    "numero": 2489942194,
    "casado": False,
    "codigo": 214
}

print(dic["nombre"])

for key, Value in dic.items():
    print(key, Value)

frutas={
    "manzanas": 1500,
    "frutilla": 1600,
    "durazno": 3800
}

print(frutas)
frutas["pera"]=1200
print(frutas)

fru=input("Ingrese la fruta: ")
val=input("Ingrese el precio: ")
frutas[fru]=val
print(frutas)