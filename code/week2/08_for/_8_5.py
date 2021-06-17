# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 08: Δομή επανάληψης for
# Άσκηση 8_5
dd = {1: 30, 8:20, 2: 40}

for i in dd:
    print(i,'->', dd[i])
print(20*'-')

for i in sorted(dd):
    print(i, '->', dd[i])
print(20*'-')

for i in sorted(dd, key = dd.get):
    print(i, '->', dd[i])
print(20*'-')
