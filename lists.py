#lists jeb saraksti
#[1,2,2,"teksts", 3.56, [1, "objekts"]]
my_list=["STRING",100,23.5]
print(my_list)
print(len(my_list))

mylist=["viens", "divi", "trīs", "četri"]
print(mylist)
print(mylist[2]) #izdrukā elementu ar norādīto ideksu
print(mylist[1:]) #izdrukā no 1 indeksa līdz beigām

#sarakstu apvienošana (konkatinācija)
cits_list=["pieci", "seši"]
print(mylist+cits_list)
jauns_list =mylist + cits_list
print(jauns_list)

#saraksta mainīšana
jauns_list[0] = 1 #definē konkrētā elementa vērrtību
print(jauns_list)
jauns_list.append("septiņi")
print(jauns_list)
jauns_list.append(8)
print(jauns_list)

#elementu noņemšana
pop_elem = jauns_list.pop()
print(pop_elem)
print(jauns_list)
jauns_list.pop(3) # izņem no saraksta elementu ar norādito indeksu
print(jauns_list)

#elementu kārtošana
new_list=["b", "a", "e", "c"]
num_list=[4, 1, 8, 3]
new_list.sort()
print(new_list)
num_list.sort()
print(num_list)
new_list.reverse()
print(new_list)

#MyList = [1, 2, 3, 100, "tu", 3.59, "skaista!"]
#MyList.sort()
#print(mylist)

nested_list = [2,4,[5,8]]
print(len(nested_list))
print(nested_list[1])
print(nested_list[2][1]) #izdruka ligzdsaraksta elementu

augli = ["ābols", "banāns", "gurķis"]
print(augli[2])
augli[2]="apelsīns"
print(augli)
augli.append("bumbieris")
print(augli)
augli.insert(2, "citrons")
print(augli)
augli.pop(1)
print(augli)
augli.sort()
print(augli)
print(f"šajā sarakstā ir {len(augli)} augli")