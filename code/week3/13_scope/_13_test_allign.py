# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 13: Εμβέλεια μεταβλητών
# Άσκηση 13_test_allign
st = 'Αιγαίο, με βελτίωση του'

def allign_text(line, width):
        sp = ' '
        extra_spaces = width- len(line)
        print(line, extra_spaces)
        if sp in line:
            while extra_spaces > 0 :
                line = line.replace(sp, sp+' ', extra_spaces)
                print(line)
                extra_spaces = width- len(line)
                sp += ' '
            return line
        else:
            return line
print(st)
print(allign_text(st, 30))
