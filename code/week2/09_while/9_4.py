# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 9. Δομή while

# βρες το άθροισμα και το γινόμενο 2 ακεραίων
ans = ""

while ans != "stop" :
    x = input("x=")
    y = input("y=")
    if not(x.isdigit() and y.isdigit()):
        continue
    else:
        x = int(x)
        y = int(y)
        print("x+y = {}, x*y = {}".format(x+y, x*y))
        ans = input("Να συνεχίσω; stop για έξοδο")
        if ans == "stop":
            break
