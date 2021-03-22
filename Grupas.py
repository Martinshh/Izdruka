#Izveido kodu kas izvadīs no viens līdz ievadītajam naturālajam skaitlim kopējo faktoriālo summu.

n=int(input("Ievadi naturālu skaitli:"))
while True:
  if n<1:
    n=int(input("Ievadi naturālu skaitli:"))
  else:
    break
faktorials=1
summa=0
for i in range(n):
  faktorials= faktorials*(i+1)
  summa=summa + faktorials
  print(faktorials,summa)

print (f"Pirmo {n} skaitļu faktoriālu summa ir {summa}.")