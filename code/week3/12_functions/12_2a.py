# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 12. Functions

'''12.2 Να κατασκευάσετε πρόγραμμα που ζητάει
διαδοχικά από τον χρήστη την ακτίνα σφαίρας
και υπολογίζει, καλώντας σχετικές συναρτήσεις
την επιφάνεια και τον όγκο της.
Τερματίζει με stop.
e = 4*pi*r**2
v = (4/3)*pi*r**3
'''
import math
pi = math.pi

def area(r):
    # συνάρτηση υπολογισμού επιφάνειας σφαίρας
    return 4*pi*r**2

def vol(r):
    # συνάρτηση υπολογισμού όγκου σφαίρας
    return (4/3)*pi*r**3
    
def isnum(n):
    # συνάρτηση που βρίσκει αν συμβολοσειρά είναι αριθμός
    if not type(n) is str :
        return False
    n = n.strip()
    if n.isdigit():
        return True
    elif n[0] in '+-' and isnum(n[1:]):
        return True
    elif "." in n:
        if n.count(".") == 1 and isnum(n.replace(".","")):
            return True
        else:
            return False
    else:
        return False

while True:
    r = input("R=")
    if r == 'stop' : break
    if isnum(r):
        v = vol(float(r))
        e = area(float(r))
        print("Επιφάνεια={:1.2f}, Όγκος={:1.2f}".format(e,v))
    else:
        continue              
              
