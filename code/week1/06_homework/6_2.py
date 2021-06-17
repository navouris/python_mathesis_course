# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 6. Ασκήσεις

# Άσκηση 6.2

epafes = {"Νίκος" : 111222, "Μαρία" : 333444}
# εισαγωγή νέας επαφής
print("Οι επαφές είναι: \n", epafes)
print ("Δώσε μια νέα επαφή: ")
name = input("Δώσε όνομα:")
tel = input("Δώσε αριθμό τηλεφώνου:")
epafes[name] = int(tel)
print("Οι επαφές είναι : \n", epafes)
# ταξινόμηση επαφών
epafes_list = list(epafes.items())
epafes_list.sort()
print("Η ταξινομημένη λίστα επαφών είναι:\n", epafes_list)

