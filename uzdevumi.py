#1.uzdevums
x = input("Ievadi tekstu!: ")
print(len(x))

#2.uzdevums 
m = input("Ieraksti ko gribi: ")
print(m[0])

#3.uzdevums
myString = ("Sveika, Pasaule!")
print(myString[-6:-1])

#4.uzdevums
i = input("Ievadi jebko!: ")
print(i.upper())

#5.uzdevums
o = input("Ievadi jebko!: ")
print(o.lower())

#6.uzdevums
vards = "samērcēt"
ped_burti = vards[1:]
print("p"+ped_burti)

#7.uzdveums
g ="  Sveika, pasaule!"
print(g.strip())


#8Uzdevums:
#Izveidot programmu, kura vārdam nomaina pirmo burtu uz lielo
#Piemērs:

#Ievade: martins
#Izvade: Martins

vards = input("Ievadi savu vārdu: ").capitalize()
print(vards)


#9.uzdevums
vards = str(input("Ievadi vārdu: "))
pirmais_b = vards[0]
vards = vards.lower()
vards = vards[::-1]
vards = vards.capitalize()
print(vards+". Pamatīgs juceklis, vai ne,",pirmais_b)

