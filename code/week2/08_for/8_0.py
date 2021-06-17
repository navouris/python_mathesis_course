# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 8. Δομή for


li = [ 1, 8, 11, 34, 45, 78, 23, 99]
key = int(input("δώσε κλειδί:"))
for item in li:
    if item == key:
        print("βρέθηκε το ", key)
        break
else:
    print("δεν βρέθηκε το ", key)
          
