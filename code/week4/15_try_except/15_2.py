# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 15. Δομή try/except

# άσκηση 15.1 βρες το πηλίκο και το υπόλοιπο της διαίρεσης 2 ακεραίων
ans = ""

while ans != "stop" :
    x, y = " ", " "
    while type(x) is str or type(y) is str :
        try:
            x = int(input("x=").strip())
            y = int(input("y=").strip())
            print("x/y = {}, x%y = {}".format(x/y, x%y))
        except ValueError as e :
            print('Δώστε ακέραιο\n', e)
        except ZeroDivisionError as e:
            print("προσοχή όχι διαίρεση με 0\n", e)
        finally :
            ans = input("Να συνεχίσω; stop για έξοδο")
            if ans == "stop":
                break
