my_tup =(1, 2, 3)
my_list=[1, 2, 3]
print(type(my_tup))
print(type(my_list))
print(len(my_tup))

my_tup=("viens", "seši", 6, 34.5)
print(my_tup)

print(my_tup[0])
print(my_tup[-1])
print(my_tup.count("viens"))
print(my_tup.index(6))
my_list[0] = "new"
print(my_list)

#sets
my_set = set()
print(my_set)
my_set.add(1)
print(my_set) #ievieto figuriekavas, bet  nav pāri 
my_set.add(5)
print(my_set)
my_set.add(3.4)
print(my_set)
my_set.add(5)
print(my_set)


#piemērs
s= "Salaspils"
my_set = set(s)
print(my_set)

#booleans - true or false - izmanto loģiskajos operators
print(True)
print(type(False))

#piemērs
print(1 > 2)
print(1 == 1)
