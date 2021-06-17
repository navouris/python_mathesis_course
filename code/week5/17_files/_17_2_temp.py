# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 17: Αρχεία
# Άσκηση 17_2_temp
# Άσκηση 17.2
import calendar
while True:
    year = input('έτος - enter για έξοδο :')
    if year == '':
        break
    try:
        year = int(year)
    except ValueError:
        continue
    if type(year) is int :
        my_year = calendar.calendar(year)
        print(my_year)
        with open(str(year)+'_en.txt', 'w', encoding = 'utf-8') as f:
            f.write(my_year)
        with open('months.csv', 'r', encoding = 'utf-8') as f:
            for m in f:
                m_en = m.split(',')[0]
                m_gr = m.split(',')[1].strip()
                my_year = my_year.replace(m_en, m_gr)
        my_year = my_year.replace('Mo Tu We Th Fr Sa Su', 'Δε Τρ Τε Πε Πα Σα Κυ')
        print(my_year)
        with open(str(year)+'_gr.txt', 'w', encoding = 'utf-8') as f:
            f.write(my_year)
        
        
            


