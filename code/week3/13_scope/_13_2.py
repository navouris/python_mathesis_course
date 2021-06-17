# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 13: Εμβέλεια μεταβλητών
# Άσκηση 13_2
def f2():
    #global name
    #name = "Μαρία"
    print(name)

def f1():
    global name
    name = "Κώστας"
    f2()

# κυρίως πρόγραμμα
name = "Γιώργος"
f1()
print(name)
    
