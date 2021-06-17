# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 18: Σύνδεση με το λειτουργικό σύστημα
# Άσκηση 18_2temp
# Άσκηση 18.2
'''
Για τον φάκελο των προσωπικών αρχείων σας στον υπολογιστή σας
και όλους τους υπο-φακέλους του:
(α) Να καταγράψετε το πλήθος
αρχείων ανά κατηγορία αρχείων
(β) Να βρείτε το ποσοστό χώρου
που καταλαμβάνει η κάθε κατηγορία.
os.path.getsize
'''
import os
import os.path

while True:
    dir =input('Αρχικός φάκελος:')
    if dir == '': break
    if os.path.isdir(dir):
        file_types= {}
        file_size= {}
        for r,d,f in os.walk(dir):
            for fi in f:
                if fi[0] not in '.~':
                    # τύπος αρχείου
                    f_parts = fi.split('.')
                    if len(f_parts) > 1:
                        f_type = f_parts[-1]
                        file_types[f_type] = file_types.get(f_type, 0) +1
                        # μέγεθος αρχείου
                        full_f_name = os.path.join(r,fi)
                        size = os.path.getsize(full_f_name)
                        file_size[f_type] = file_size.get(f_type, 0) + size
    for t in file_types:
        print(t,'\t\t', file_types[t])
    print(50*'*')
    total_size = sum(file_size.values())
    print("Συνολικό μέγεθος:", total_size)
    for t in file_size:
        percent = 100*file_size[t]/total_size
        print('{}\t\t{}\t\t{:5.2f}%'.format(t, file_size[t], percent))
