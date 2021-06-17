# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 17: Αρχεία
# Άσκηση 17_3b
import calendar

def replace_center(m_en, m_gr):
    global my_year
    l_en = len(m_en)
    l_gr = len(m_gr)
    l_dif = l_gr - l_en # Οι μήνες στα Ελληνικά > από τους αντίστοιχους Αγγλικούς
    leading_spaces = l_dif//2
    trailing_spaces = l_dif - leading_spaces
    to_replace = leading_spaces * " " + m_en + trailing_spaces * " "
    if to_replace not in my_year: # αν ο μήνας στο τέλος της γραμμής
        to_replace = leading_spaces * " " + m_en
    my_year = my_year.replace(to_replace, m_gr)
    
while True:
    year = input("Έτος(enter για έξοδο) :")
    if year == '':
        break
    try:
        year = int(year)
    except ValueError:
        continue
    my_year = calendar.calendar(year)
    my_year = my_year.replace("Mo Tu We Th Fr Sa Su", "Δε Τρ Τε Πε Πα Σα Κυ")
    en_gr = {}
    filename = str(year)+'.txt'
    with open(filename, "w", encoding="utf-8") as newfile:
        with open("months.csv", "r", encoding="utf-8") as months_file:
            for line in months_file:
                new_line = line.strip()
                new_line = new_line.split(",")
                en_m = new_line[0]
                gr_m = new_line[1]
                en_gr [en_m] = gr_m
                #my_year = my_year.replace(en_m, gr_m)
                replace_center(en_m, gr_m)
    print(my_year, str(year))
    print(my_year.find(str(year)))
    input()
    my_year = my_year.replace(8*" "+str(year), "Hμερολόγιο του "+ str(year))
    print(my_year)
    with open(str(year)+".txt", "w", encoding="utf-8") as f:
        f.write(my_year)



