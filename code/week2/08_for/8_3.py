# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 8. Δομή for

# Άσκηση 8.3
#Να δημιουργήσετε μια λίστα με μέλη
#τα γράμματα μιας συμβολοσειράς

st = "καλή σας μέρα αρχόντες"

li = []
for ch in st:
    if ch.isalpha():
        li.append(ch)

print(li)
    


 
