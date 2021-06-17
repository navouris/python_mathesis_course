# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 6. Ασκήσεις

# Άσκηση 6.3

poem = '''
Εγώ μετράω τα ρέστα μου να βγάλω κι άλλο μήνα
ανοίγω και δε βλέπω ουρανό 
εσύ έχεις στο πιάτο σου ολόκληρη Αθήνα
ανοίγεις και χαζεύεις το κενό
'''

print(poem)

# αλφαβητική λίστα λέξεων

list_words = poem.split()
list_words.sort()
print(list_words)

# πλήθος λέξεων

print("Το πλήθος λέξεων είναι: {}".format(len(list_words)))

# πλήθος χαρακτήρων

poem = poem.replace(" ", "").replace("\n", "")
print("Το πλήθος γραμμάτων είναι: {}".format(len(poem)))

