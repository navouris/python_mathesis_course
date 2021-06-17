# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 8. Δομή for

# Άσκηση 8.1
#Να τυπώσετε διδιάστατη λίστα 3 χ 4

epafes = {
    "Νίκος"    	:        1234567,
    "Κώστας"    	:        8889990,
    "Μαρία"     	:        4446699 }


for e in sorted(epafes) :
    print("{:15s}\t: {:10d}".format(e, epafes[e]))


 
