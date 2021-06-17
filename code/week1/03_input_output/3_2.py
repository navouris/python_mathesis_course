# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 3. input/ output

C = input("δώσε θερμοκρασία σε βαθμούς Κελσίου:")
C = float(C)
F = C*1.8+32
print("Η θερμοκρασία σε βαθμούς Φαρενάιτ είναι {:1.2f}" .format(F))
