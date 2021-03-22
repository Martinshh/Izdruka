"""
print("sveiki")
print("sveiki")
print("sveiki")
print("sveiki")
print("sveiki")
print("sveiki")

#while True:
#   #print("sveiki")

i = 0 #tipisks cikla mainigais
while i<5:
    print("sveiki")
    i += 1 # i=i+1  lai palielnatu i
print("i tagad ir", i)

j=10
while j<5:
    print("Sveiki, nr.",j)
    j+=1

while i>0:
    print("skaitam atpakal:", i)
    i-=1
#ar soli 2
i=20
while True:
    print("i ir", i)
    if i>26:
        break
    i += 2

#ievadiet eglites augstumu
#izdrukat egliti:
#piem. augstums == 3

augstums = int(input("cik stavu bus eglei?"))
i = 0
while i<augstums:
    print("*"*augstums)
    i+=1
"""

sk=1
a= ""
for sk in range(sk, 5):
    a = a+ str(sk)
    print(a)

sk=1
a=""
while sk < 5:
    a = a + str(sk)
    print(a)
    sk +=1