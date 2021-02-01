#Komentārus var raskstīt
#vairākās 
#rindās"""
print ("Sveika,pasaule!")
print (2*2)
print (2*2, 2*3, 2*4, "Pitons")
print (f"ja saskaitīsim 5 ar 7 , iegūsim {5+7}.")
print ("Sveika,"+"pasaule!")#var rakstīt komentārus
print("Mārtiņš")
print("Mārtiņš")
print("Mārtiņš")
print("Mārtiņš")
print("Mārtiņš "*7)
print (f"Lai aprēķinātu cik gadā ir sekundes ir 60 sekundes (1 minūte) x 60 minūtes (1 stunda) x 24 stundas (1 diennakts) x 365 diennaktis, iegūsim {60*60*24*365}.")
print ()

#Mainīgie
a=5
print(a)
print (a+a)
a=a + a + a #Ar = piešķir vērtību
print(a)
print (type(a))
a=30.1
print (type(a))
mani_ienakumi=437
nodoklis = 0.23 #tas ir 10%
maniNodokli = mani_ienakumi*nodoklis
print(maniNodokli)
#help
help("keywords")

#Datu ievade
print("Ievadi vārdu: ")
x = input()
print ("Tavs ievadītais vards ir "+ x)

x=input ("Ievadi vārdu:")
print("Tavs ievadītais vārds ir " + x)

x= int(input("Ievadi skaitli: "))
print (f"Tavs ievadītais skaitlis ir {x}.")