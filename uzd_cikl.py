"""
#1.uzd
a = int(input("Ievadi veselu skaitli: "))
for skaitlis in range(0, a+1):
    if skaitlis % 2 != 0:
        print(skaitlis)

#2.uzd
a = int(input("Ievadi sākuma skaitli: "))
b = int(input("Ievadi beigu skaitli: "))
if a<b:
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)
 


#3.uzd
a = int(input("Ievadi veselu skaitli: "))
for i in range(a,0-1,-1):
    if i % 2 != 0:
        print(i)


myList = []
for i in range(10):
    n = float(input(f"Ievadi {i+1}. skaitli: "))
    myList.append(n)
print(myList)
"""
n = 0 
while n < 2:
    n=int(input("Ievadi veselu skaitli, kas ir vismaz 2: "))

dalitajs = 2
while True:
    if n % dalitajs == 0:
        print (f"Mazākais skaitlis ar ko {n} dalās bez atlikuma ir {dalitajs}")
        break
    else:
        dalitajs +=1

    