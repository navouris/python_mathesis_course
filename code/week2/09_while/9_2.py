# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 9. Δομή while

# πότε θα γίνω εκατομμυριούχος αν έχω Χ ευρώ και το επιτόκιο είναι ε %

x, e = 0, 0
while x<= 0 or e <= 0 : # θα πρέπει να δώσει θετικούς αριθμούς
    x = float(input("πόσα χρήματα έχεις;"))
    e = float(input("ετήσιο επιτόκιο %:").replace("%",""))
year = 0
while x < 1E6 :
    year += 1
    x = x * (1+e/100)
else:
    print("σε {} χρόνια".format(year))
    
