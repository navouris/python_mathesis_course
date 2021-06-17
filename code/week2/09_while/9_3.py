# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 9. Δομή while

# διάβασε διψήφιο αριθμό

num = 0

while num > 99 or num < 10 :
    num = int(input("δώσε θετικό διψήφιο αριθμό:"))
else :
    print("ευχαριστώ, έδωσες το {:2d}".format(num))
    
