# άσκηση 15.1 βρες το πηλίκο και το υπόλοιπο της διαίρεσης 2 ακεραίων
# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 15: Διαχείριση εξαιρέσεων
ans = ""
while ans != "stop" :
    x, y = " ", " "
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
