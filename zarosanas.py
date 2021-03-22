#if ,else ,elif
#if nosacījums:
    #izpildāmā darbība
#elif cits nosacījums:
    #izpildāmā darbība
#else:
    #noklusētā darbība(visi citi gadījumi)
#ja skailits ir lielaks par 5 tad izdrukā ,bet ja lielaks par 5 tad citādi,
#ja skaitlis lielaks par 0 tad izdrukā , ka lielāks par 0
#citādi izdrukā ka tas nav pozitivs skaitlis.

a = -1
if a>5:
    print("skaitlis ir lielaks par 5.")
elif a>0:
    print("skaitlis ir lielāks par 0.")
else:
    print("skaitlis nav pozitīvs.")

if True:
    print("Patiesi")

suns_grib_est = False
if suns_grib_est:
    print("pabaro suni!")
else:
    print("suns jau ir paedis")