# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 14: Βιβλιοθήκες
# Άσκηση 14_3
import math

def ypot(a,b) :
    '''
    INPUT : a, b οι κάθετες πλευρές ενός ορθογωνίου τριγώνου
    OUTPUT: η υποτείνουσα, ή False αν κάποιο από τα a,b δεν είναι αριθμός
    '''
    if ((type(a) is int or type(a) is float) and
    (type(b) is int or type(b) is float) ) :
        c = math.sqrt(math.pow(a,2) + math.pow(b,2))
        return c
    else:
        return False

print(ypot(3,4))
