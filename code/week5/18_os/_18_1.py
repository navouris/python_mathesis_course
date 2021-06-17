# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 18: Σύνδεση με το λειτουργικό σύστημα
# Άσκηση 18_1
import os
import os.path

def list_files(start_path):
    max_count = 50
    count = 0
    for root, dirs, files in os.walk(start_path):
        level = root.replace(start_path, '').count(os.sep)
        indent = ' ' * 8 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            if f[0] != '.' and f[0] != "~":
                print('{}{}'.format(sub_indent, f))
                count +=1
                if count%max_count == 0:
                    x = input('..... συνέχεια, [x για έξοδο]:')
                    if x == '' or x not in "xXχΧ":
                        continue
                    else:
                        return(-1)
    print("Βρέθηκαν {} αρχεία".format(count))
    return(0)

def main():
    while True:
        dir = input('Δώσε αρχικό φάκελο [enter για έξοδο]:')
        if dir == '':
            break
        elif os.path.isdir(dir):
            x = list_files(dir)
            if x == -1 :
                break
        else:
            print('Δεν βρέθηκε ο φάκελος {}'.format(dir))

if __name__ == '__main__':
    main()
