# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 14: Βιβλιοθήκες
# Άσκηση 14_1
import random
next = ''
while next ==  '' :
    randnum = random.randint(1,100)
    randint = random.randint(1,50) + randnum
    randnew = random.randint(1,10) + randint
    print(randnum, randint, randnew)
    next = input()
