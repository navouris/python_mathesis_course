# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 14: Βιβλιοθήκες
# Άσκηση 14_2
import a
num = ' '
while True :
    num = input('δώσε αριθμό:')
    if num == '' : break
    num = a.abs(num)
    if num :
        print("η απόλυτη τιμή του είναι {}".format(num))
    else:
        print("δεν είναι αριθμός!!!")
