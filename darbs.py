"""
a = 15
b = 2.5
c = 4.78
if a > b and a > c and b < a and b < c:
    print("Skaitlis b ir vismazākais un skaitlis a ir visslielākais")
elif a < b and a < c and b > a and b > c:
    print("Skaitlis a ir vissmazākais un skaitlis b ir visslielākais")
else:
    print("Parbaudi visus skaitļus")


temperatura = float(input("Ievadiet savu temperatūru "))
if temperatura < 35:
    print("Vai nav par aukstu?")
elif 35 <= temperatura <= 37:
    print("Viss kārtībā")
else:
    print("Iespējams drudzis")


myList = [a,b,c]
myList.sort()
print(f"Lielakais skaitlis ir {myList[-1]}, bet mazakais skaitlis ir {myList[0]}.")
"""

atr= "veikals"
#banka, veikals, aptieka
if atr == "veikals":
    print("Janoperk abols")
elif atr == "banka":
    print("Te ir daudz naudas")
elif atr == "aptieka":
    print("Japerk tabletkas")
else:
    print("abolu nav")