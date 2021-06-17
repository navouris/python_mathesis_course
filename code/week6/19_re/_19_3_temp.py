# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 19: Regular Expressions
# Άσκηση 19_3_temp
# Μάθημα 19
# Άσκηση 19.3
'''
Στο παράδειγμα της ενότητας 17 (αρχεία), είχαμε επεξεργαστεί το
αρχείο vouna.txt χρησιμοποιώντας μεθόδους συμβολοσειρών.
Να επεκτείνετε την άσκηση ώστε να περιλάβετε τη γεωγραφική περιοχή
κάθε βουνού, χρησιμοποιώντας regular expressions.

'''
import re
with open('vouna.txt', 'r', encoding = 'utf-8') as f :
    vouna = []
    for vouno in f:
        vouno = vouno.split('\t')
        name = vouno[0]
        height = vouno[1]
        region = vouno[2]
        vouna.append((name,height, region))
for v in vouna:
    print(v)

max_height = 0
for v in vouna:
    if int(v[1]) > max_height: max_height = int(v[1])
print('Το ψηλότερο βουνό έχει ύψος', max_height)
to_file = ''
with open('vouna2.txt', 'w', encoding='utf-8') as f:
    for v in vouna:
        region = re.sub(r'\([^)]*\)', '', v[2]).split(',')
        print(region)
        to_file += 'Το όρος {} έχει ύψος {} μέτρα. '.format(v[0],v[1])
        v_height = int(v[1])
        if v_height == max_height:
            to_file += "Είναι το ψηλότερο ελληνικό βουνό,"
        else :
            diff = max_height - v_height
            to_file += "Είναι {} μ. χαμηλότερο,".format(diff)
        ## Προσθήκη αναφοράς στην περιοχή
        to_file += " και βρίσκεται στη "
        for r in region:
            r_name = r.rstrip()
            if r_name[-1] == 'ς' : r_name = r_name[:-1]
            if region.index(r) == 0 : kai = ' '+r_name
            else: kai = ' και στη '+ r_name
            to_file += kai
        to_file += '.'
    print(to_file)
    f.write(to_file)
