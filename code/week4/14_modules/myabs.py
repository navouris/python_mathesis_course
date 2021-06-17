# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 14: Βιβλιοθήκες
# Άσκηση myabs
# βιβλιοθήκη συνάρτησης abs που δέχεται συμβολοσειρές (εκδ. 1.1)

def abs(x):
    if type(x) is str:
        if __is_int(x): x = int(x)
        elif __is_float(x): x = float(x)
        elif 'E' in x.upper():
            num = x.upper().split('E')
            if __is_float(num[0]) and __is_int(num[1]) :
                x = float(x)
    if type(x) is int or type(x) is float:
        if x <0 : return -x
        else: return x

def __is_int(x):
    # -10 +20
    if x.count('+')> 1 or x.count('-')>1 : return False
    if x.strip().lstrip('-').isdigit() or \
       x.strip().lstrip('+').isdigit() :
        return True
    else:
        return False

def __is_float(x):
    if x.count('+')> 1 or x.count('-')>1 : return False
    if x.strip().lstrip('-').replace('.','',1).isdigit() or\
       x.strip().lstrip('+').replace('.','',1).isdigit() :
        return True
    else: 
        return False
