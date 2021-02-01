tel = {"direktors": "6757272", "vietnieks": "67571275", "sekretāre": "6752323"}

print(tel["direktors"]) #norādot atslēgu, izdrukā vērtību

cenas = {"piens":1.12, "āboli":1.15, "apelsīni":1.25}
print(cenas)
print(cenas["piens"])

d = {"k1": 123, "k2":[10,11,12], "k3":{"atsl1": 100}}
#vāŗdnīcas var uzglabāt dazādus datu tipus, tai skaitā list un vārdnīcas
print(d["k2"])
print(d["k3"])
print(d["k2"][2]) #izdrukā elementu ar noradīto indeksu un atslegu.
print(d["k3"]["atsl1"]) #izdrukā ligzdvārdu elementus