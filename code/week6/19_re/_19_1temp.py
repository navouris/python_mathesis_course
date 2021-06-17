# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 19: Regular Expressions
# Άσκηση 19_1temp
import os
import os.path
import re

dir = '/Volumes/nma1000\ 1/python_mathesis/code/19_re'
print(os.listdir(dir))
tw = os.path.join(dir, 'trivizas_works.txt')
try:
    with open(tw, 'r', encoding = 'utf-8') as f:
        works = f.read()
        for l in works: print(l)
except IOError as e:
    print(e)


