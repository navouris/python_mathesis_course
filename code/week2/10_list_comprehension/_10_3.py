# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 10: Συνοπτικές λίστες - list comprehension
# Άσκηση 10_3
dates = []
import random

while True:
    y = input("έτος: ")
    if y == "": break
    dates = []
    for i in range(10):
        m = random.randint(1,12)
        d = random.randint(1,31)
        # DD-MM-YYYY
        dates.append("{:02d}-{:02d}-{:4s}".format(d,m,y))
    print(dates)


        
    
    


    
