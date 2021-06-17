# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 19: Regular Expressions
# Άσκηση 19_2
# Μάθημα 19
# Άσκηση 19.2
'''
Να βρείτε αν υπάρχει email στη σελίδα.
Να βρείτε το περιεχόμενο της ετικέτας <title>
.
Να βρείτε το περιεχόμενο των ετικετών <h2> της σελίδας αυτής.
'''

import re

with open('upatras.html', 'r', encoding = 'utf-8') as f:
    html = f.read()

#print(html)

email_pattern = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'

print('Αναζήτηση email στην ιστοσελίδα')
found = re.findall(email_pattern, html, re.I)
found = list(set(found))
for f in found :print('\t\t', f)

while True:
    tag = input('Δώσε ετικέτα:')
    if tag == '': break
    tag_pattern = r'<'+tag+r'\b[^>]*>(.*?)</'+tag+r'>'
    found = re.findall(tag_pattern, html, re.I)
    found = list(set(found))
    for f in found :print('\t\t', f)

