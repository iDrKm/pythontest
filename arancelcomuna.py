arancel=200000
dcto=0
print(""" Escoga su comuna
      1. La florida
      2. Puente Alto
      3. La pintana
      4. San Joaquin""")
comuna=int(input("Seleccione su comuna: "))
if comuna==1:
    dcto=20
elif comuna==2:
    dcto=25
elif comuna==3:
    dcto=30
elif comuna==4:
    dcto=15
else:
    print("Opcion incorrecta")

GrupFam=int(input("Cuantas personas viven con usted incluido: "))
if GrupFam==1:
    dcto+=2
elif GrupFam<=4 and GrupFam>=2:
    dcto+=3
elif GrupFam>=5:
    dcto+=4
else:
    print("Seleccion Incorecta")

print("el descuento es: ", dcto , "%")
desc=arancel*dcto/100
total=arancel-desc
print("el total a pagar es $", total)
    



      

