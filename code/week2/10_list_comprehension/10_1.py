# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 10. list compehension

# Παράδειγμα 1
# Να βρείτε τους αριθμούς που είναι πολλαπλάσια του 2
# και πολλαπλάσια του 3 από το 1 ως το 20

# λύση με for

n = []
for i in range(1,21):
    if i%2 == 0 and i%3 == 0 :
        n.append(i)
print(n)

# λύση με list comprehension

n = [ x for x in range(1,21) if x%2 == 0 and x%3 == 0 ]
print(n)

# Παράδειγμα 2.
#Έστω λίστα L = [5,8,12,7] Να δημιουργήσετε νέα λίστα με
#στοιχεία τα μέλη της L που είναι περιττοί αριθμοί αυξημένοι κατά 10.

# λύση με for

L = [5,8,12,7]
L1 = []
for i in L :
    if i%2 == 1 :
        L1.append(i+10)
L = L1
print(L)

# λύση με list comprehension

L = [5,8,12,7]
L = [x+10 for x in L if x%2 == 1]
print(L)

# Παράδειγμα 3.
# Έστω s1 = "αβγ” και s2 = "χψω" να δημιουργή-σετε λίστα με όλους
# τους συνδυασμούς των χαρακτήρων του s1 με αυτούς του s2.  

s1 = "αβγ"
s2 = "χψω"
# λύση με for
res = []
for x in s1:
    for y in s2:
        res.append(x + y)
print(res)

#λύση με list comprehension
res = [x + y for x in s1 for y in s2]
print(res)
