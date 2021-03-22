#iterācija=kādas darbības atkārtota izpilde
mainigais = [1,2,3,4]
for varde in mainigais:
    print(varde)

myList=[1,2,3,4,5,6,7,8,9,10]
for mamma in myList:
    print("Sveiki")

for sk in myList:
    if sk%2==0:
        print(sk)
    else:
         print(f"Nepāra skaitlis: {sk}")

#aprēķina summu
summa=0
for sk in myList:
    summa=summa + sk
    print(f"Summa pēc {sk} skaitļiem ir {summa}")
print(summa)

#drukā tekstu
myString = "Sveika pasaule!"
for burts in myString:
    print(burts)

for burts in "programma":
    print(burts, end =" ")

#drukā tuple
tup=(1,2,3,4)
for elements in tup:
    print(elements)

myList = [(1,2), (3,4), (5,6), (7,8)] #packed tuples
print(len(myList))

for elements in myList:
    print(elements)

for (a,b) in myList: #tuple unpacking
    print(a)
for a,b in myList: #var nelikt iekavas
    print(a)
    print(b)

myList=[(1,2,3), (4,5,6), (7,8,9)]
for a,b,c in myList:
    print(b)

#vārdnīcas
d={"k1":11, "k2":12, "k3":13}
for elements in d:
    print(elements) #izdrukā tikai atslegas

for elements in d.items():
    print(elements) #izdrukā atslegu,vērtību pārus

for atslega,vertiba in d.items():
    print(vertiba)

#Given an integer N, print all numbers from 1 to N.
n = int(input("Ievadiet veselu skaitli"))
for skaitlis in range(n):
    print(skaitlis+1)

for skaitlis in range(2, n):
    print(skaitlis+1)

for skaitlis in range(2,n,3):
    print(skaitlis)
