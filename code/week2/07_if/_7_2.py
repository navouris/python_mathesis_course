# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 07: Δομή επιλογής  if
# Άσκηση 7_2
v = int(input("Βαθμός πτυχίου: "))
v = input("βαθμός :")
v = float(v)
if  v >= 5 and v <= 10:
    print("πέρασες")
    print("συγχαρητήρια!!")
elif v<5 and v >= 0 :
    print("κόπηκες")
    print("ξαναπροσπάθησε!!!")
else:
    print("έχει γίνει κάποιο λάθος ο βαθμός μεταξύ 0 και 10")
