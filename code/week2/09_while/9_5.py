# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 9. Δομή while

# άσκηση 9.3 βρες το πηλίκο και το υπόλοιπο της διαίρεσης 2 ακεραίων
ans = ""

while ans != "stop" :
    x = input("x=").strip()
    y = input("y=").strip()
    if (x.isdigit() or (x[0] == "-" and x[1:].isdigit() )) and \
    (y.isdigit() or (y[0] == "-" and y[1:].isdigit() )) :
        x = int(x)
        y = int(y)
        if y != 0 :
            print("x*y = {}, x/y = {}".format(x*y, x/y))
        else:
            print("προσοχή όχι διαίρεση με 0")
        ans = input("Να συνεχίσω; stop για έξοδο")
        if ans == "stop":
            break
    else :
        continue
