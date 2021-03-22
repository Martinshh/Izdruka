#vienkārši piepildīt list ar elementiem
saraksts = list(range(0,11,2))
print(saraksts)

#enumerate - parāda indeksus tuplē formā
vards = "pasaule"
for i in enumerate(vards):
  print(i)


#atpakojot tuples
vards = "pasaule"
for indekss,burts in enumerate(vards):
  print(indekss)
  print(burts)
  print("\n")


#izmanto zip-sapako vairākus list  kopā kā tuplē
myList1 = [1, 2, 3]
myList2 =  ["a", "b", "c"]
for i in zip(myList1, myList2):
  print(i)

myList3 = [100,200,300,400]
for i in zip(myList1, myList2, myList3):
  print(i)

#ja kādā no list ir vairāk elemntu, rezūltāts būs tāds pats, jo zip paņemt tik, cik mazākajā 
#izmanto in , lai noskaidrotu vai objektā  atrodams meklētais elements
print("x" in [1,2,3])
print(2 in [1,2,3])
print("a" in "pasaule")
print("mykey" in  {"mykey":345})
d = {"mykey": 345}
print(345 in d.keys())
print(345 in d.values())

#min un max
myList = [10,20,30,40,100]
print(min(myList))
print(max(myList))

#bibliotēku importēšana
from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
print(mylist)
shuffle(mylist)
print(mylist)

from random import randint
print(randint(0, 100))
