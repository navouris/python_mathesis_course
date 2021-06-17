# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 10. list compehension



# Παράδειγμα 10.2 Γεννήτρια τυχαίων ημερομηνιών
import random
months = '''Ιανουάριος (31 ημέρες)
Φεβρουάριος (28 ή 29 ημέρες)
Μάρτιος (31 ημέρες)
Απρίλιος (30 ημέρες)
Μάιος (31 ημέρες)
Ιούνιος (30 ημέρες)
Ιούλιος (31 ημέρες)
Αύγουστος (31 ημέρες)
Σεπτέμβριος (30 ημέρες)
Οκτώβριος (31 ημέρες)
Νοέμβριος (30 ημέρες)
Δεκέμβριος (31 ημέρες)'''
tonoi = {"ά":"α",
         "έ": "ε",
         "ή": "η",
         "ί": "ι",
         "ό": "ο",
         "ύ": "υ",
         "ώ": "ω"}

month_names = [x.split()[0] for x in months.split("\n")]
print(month_names)

month_days = [int(x.split("(")[1][:2]) for x in months.split("\n")]
print(month_days)

while True:
    year = input("Έτος: ").strip()
    if not year.isdigit() : break
    else:
        y = int(year)
    leap = False
    if y%4 == 0:
        if y%100 != 0 : leap = True
    if not leap :
        if y%400 == 0 : leap = True
    if leap : month_days[1] = 29
    else : month_days[1] = 28
    print(y, month_days)
    random_days = input("Τυχαίες μέρες:")
    if not random_days.isdigit(): break
    else:
        random_days = int(random_days)
        random_d_list = []
        while len(random_d_list) < random_days:
            m = random.randint(0,11)
            d = random.randint(1,month_days[m])
            month_name = month_names[m]
            month_temp = ""
            for c in month_name:
                if c in tonoi: month_temp += tonoi[c]
                else : month_temp += c
            date = "{:02d}-{:02d}-{:04d}".format(d,m+1, y)
            month_name = month_temp.replace("ς","Υ").upper()                   
            date_ = "{:02d}-{:}-{:04d}".format(d+1,month_name, y)
            if date not in random_d_list:
                random_d_list.append(date)
                print(date)
                print(date_)
        print(random_d_list)
    






