# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 17: Αρχεία
# Άσκηση 17_1
# Μάθημα 17
# Άσκηση 17.1

with open('vouna.txt', 'r', encoding = 'utf-8') as f :
    vouna = []
    for vouno in f:
        vouno = vouno.split('\t')
        name = vouno[0]
        height = vouno[1]
        vouna.append((name,height))
for v in vouna:
    print(v)

max_height = 0
for v in vouna:
    if int(v[1]) > max_height: max_height = int(v[1])
print('Το ψηλότερο βουνό έχει ύψος', max_height)

with open('vouna2.txt', 'w', encoding='utf-8') as f:
    for v in vouna:
        to_file = 'Το όρος {} έχει ύψος {} μέτρα. '.format(v[0],v[1])
        v_height = int(v[1])
        if v_height == max_height:
            to_file += "Είναι το ψηλότερο ελληνικό βουνό."
        else :
            diff = max_height - v_height
            to_file += "Είναι {} μ. χαμηλότερο.".format(diff)
        f.write(to_file)


