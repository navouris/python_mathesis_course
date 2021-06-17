# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 19: Regular Expressions
# Άσκηση 19_3
import re
with open('vouna.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()
    for line in text.split("\n"):
        #print(line.rstrip())
        line = line.split("\t")
        oros =line[0]
        height = int(line[1])
        perioxh = line[2]
        perioxh = re.sub(r'\([^)]*\)', '', perioxh).split(",")
        #print(oros, height, perioxh)
        print("Το όρος {}, ύψους {}, βρίσκεται".format(oros, height), end = "")
        kai = ""
        for i in perioxh:
            area = i.strip()
            if area[-1] == "ς" : area = area[:-1]
            if perioxh.index(i)> 0 : kai = "και"
            if area[0].upper() in "ΑΕΗΙΟΥΩΆΈΉΊΌΎΏ": n = "ν"
            else : n = ""
            print("{} στη{} {} ".format(kai, n, area), end="")
        print()
            



