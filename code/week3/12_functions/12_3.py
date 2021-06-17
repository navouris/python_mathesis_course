# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 12. Functions

'''12.3 Να κατασκευάσετε πρόγραμμα που καλεί συνάρτηση
που μετράει τα κεφαλαία και μικρά γράμματα σε μια φράση.
'''

def count_capital_small(s):
    count_capital = 0
    count_small = 0
    for c in s:
        if c.isalpha():
            if c.lower() == c :
                count_small += 1
            else :
                count_capital += 1
    return count_capital, count_small

st = input("φράση:")
print(count_capital_small(st))
