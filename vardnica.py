tel = {"direktors": "6757272", "vietnieks": "67571275", "sekretāre": "6752323"}

print(tel["direktors"])  #norādot atslēgu, izdrukā vērtību

cenas = {"piens": 1.12, "āboli": 1.15, "apelsīni": 1.25}
print(cenas)
print(cenas["piens"])

d = {"k1": "vertiba", "k2": [10, 11, 12], "k3":{"atsl1": 100, "atsl2": 200}}
#vāŗdnīcas var uzglabāt dazādus datu tipus, tai skaitā list un vārdnīcas
print(d["k1"])
print(d["k2"])
print(d["k2"][2])  #izdrukā elementu ar noradīto indeksu un atslegu.
print(d["k3"]["atsl1"])  #izdrukā ligzdvārdu elementus
print(d["k2"][2])

my_dict = {"key1": ["a", "b", "c"]}
print(my_dict) 
my_list = my_dict["key1"]
print(my_list)
burts = my_list[2]
print(burts)
print(burts.upper()) #Izdruka lielo c kas atrodas vardnicas vertiba
print(my_dict["key1"][2].upper()) # viena rinda atlasa elementu un parveido

#pievieno jaunus objektus
new_dict = {"k1":100, "k2":200}
print(new_dict)
new_dict["k3"]=300
print(new_dict) 

#pieskir jaunu vertibu esosai atslegai
new_dict["k1"]= "simts"
print(new_dict)

#varnicu metodes
print(new_dict.keys()) #izdruka  atslegas
print(new_dict.values()) #izdruka vertibas
vertibu_list = list(new_dict.values())
print(vertibu_list)
print(new_dict.items())
print(new_dict.get("k1"))
print(new_dict.pop("k1"))
print(new_dict)