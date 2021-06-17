# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 9. Δομή while

# μενού 3 επιλογών

while True :
    e = input("Επιλέξτε¨:\n1.Επιλογή Α\n2.Επιλογή Β\n3.Έξοδος\n...")
    if e == "1":
        print("\nΕπιλογή Α\n\n")
    elif e == "2":
        print("\nΕπιλογή Β\n\n")
    elif e == "3":
        print ("\n\nΓεια σας, καλή συνέχεια")
        break
    else :
        continue
    
