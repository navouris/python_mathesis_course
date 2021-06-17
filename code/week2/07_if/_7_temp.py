# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 07: Δομή επιλογής  if
# Άσκηση 7_temp
vathmos = ("βαθμός πτυχίου;")
vathmos = float(vathmos)
if vathmos <= 10 and vathmos >= 8.5 :
    print("Άριστα")
elif vathmos < 8.5 and vathmos >= 6.5 :
    print("Λίαν καλώς")
elif vathmos < 6.5 and vathmos >= 5 :
    print("Καλώς")
else :
    print("όχι βαθμός πτυχίου")
    
