# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 13: Εμβέλεια μεταβλητών
# Άσκηση 13_1a
# συνάρτηση main.
def main():
    get_name()
    print('Γειά σου', name)
    
# συνάρτηση get_name.
def get_name():
    name =  input('Πώς σε λένε; ')
    return name

# Κλήση συνάρτησης main.
main()
