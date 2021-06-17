# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 14: Βιβλιοθήκες
# Άσκηση a
def abs(x) :
    if type(x) is str:
        if is_int(x) : x = int(x)
        elif is_float(x) : x = float(x)
        elif 'E' in x.upper():
            num = x.upper().split('E')
            if is_float(num[0]) and is_int(num[1]):
                x = float(x)           
    if type(x) is int or type(x) is float:
        if x < 0:
            return -x
        else :
            return x

def is_int(x):
    if x.strip().lstrip('-').isdigit() or \
       x.strip().lstrip('+').isdigit():
        return True
    else :
        return False
    
def is_float(x):
    if x.strip().lstrip('-').replace('.','',1).isdigit() or \
       x.strip().lstrip('+').replace('.','',1).isdigit():
        return True
    else:
        return False
