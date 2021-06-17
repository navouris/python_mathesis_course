# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 4. Λίστες - Πλειάδες

# Ορισμός
my_lista = ['Γιώργος', 3.14, 100]
print(my_lista)
print(len(my_lista))
print(my_lista[0][0])

# πράξεις - μέθοδοι
li = [1,2,3]
print(li[1:])
print(li + [4,5])
print(li*2)

my_lista = ['Γιώργος', 30, 1.85]
my_lista.append('m')
print(my_lista)
my_lista.insert(1, 'Γεωργίου')
print(my_lista)
my_lista.remove('m')
print(my_lista)
my_lista.pop(2)
print(my_lista)

print(my_lista.index(1.85))

# ταξινόμηση λιστών
li = [1,5,2,8]
li.sort()
print(li)
li.reverse()
print(li)

l1 = sorted(li)
print(li, l1)

# πολυδιάστατες λίστες

pinx = [[2,6,4,7], [1,0,3,2]]
print(pinx)
print(pinx[1][2])

# πλειάδες - tuples

tu = (1,2,3)
print(tu)
print(tu[:2])
