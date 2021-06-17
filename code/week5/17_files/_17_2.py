# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 17: Αρχεία
# Άσκηση 17_2
# Παράδειγμα δομής with
with open('vouna.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.rstrip())
