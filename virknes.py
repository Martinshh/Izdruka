"""
vards = input ("Kā tevi sauc?")
print(f"Labdien, {vards}.")

gadi = int(input("Cik tev gadi?"))
print("Tavs dzimšanas gads ir" + str (2021-gadi))
print(f"Tavs dzimšanas gads ir {2021-gadi}")

temperatūra = int(input("Cik temp ir šodien?"))
print(f"Temperatūra farengeitos ir {temperatūra * 9/5 +32}")

augstums = int(input("Ieraksti šeit telpas augstumu "))
platums = int(input("Ieraksti šeit telpas platumu "))
garums = int(input("Ieraksti šeit telpas garumu "))
print (f"Telpas tilums ir {augstums*platums*garums}")
"""
#[sākums:beigas:solis]
myString = "Sveika. pasaule!"
print(myString)
print(myString[0]) #izdrukā pirmo rakstzīmi (ar indeksu 0)
print(myString[8]) #izdrukā devīto rakstzīmi (ar indeksu 8)
print(myString[-2]) #izdrukā priekšpēdējo
print(myString[14]) #izdrukā priekšpēdējo
print(myString[-1]) #izdrukā pēdējo

myString = "abcdefghijklmnoprstuvz"
print(myString)
print(myString[2]) #izdrukā c
print(myString[2:]) #izdrukā sākot no c
print(myString[:3]) #izdrukā lidz c(beigu indeksu nedrukā)
print(myString[3:6]) #izdrukā no 3. līdz 5. indeksam
print(myString[::]) #izdrukā
print(myString[::2]) #izdrukā katru 2
print(myString[::3]) #izdrukā katru 3
print(myString[2:7:2]) #izdrukā no 2. lidz 6. indeksam katru otro.
print(myString[::-1]) #izdrukā visu otrādi