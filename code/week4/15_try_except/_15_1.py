# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 15: Διαχείριση εξαιρέσεων
# Άσκηση 15_1
x,y = " "," "
while type(x) is str or type(y) is str:
    try:
        x = int(input('x='))
        y = int(input('y='))
        d = x/y
        m = x%y
    except ValueError as e:
        print('Παρακαλώ δώστε ακέραιο')
        print(e)
    except ZeroDivisionError as e:
        print('Προσοχή διαίρεση με μηδέν')
        print(e)
        y = str(y)
        # συνέχεια προγράμματος ...
print ('ευχαριστώ, οι αριθμοί ήταν {}, {}'.format(x,y))
print('x/y={} υπόλοιπο διαίρεσης={}'.format(d,m))




    
    
