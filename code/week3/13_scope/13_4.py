# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 13. Άσκηση 
# συνάρτηση που τυπώνει κείμενο με πλάτος width

def align_text(line, width):
    extra_spaces = width - len(line)
    sp = ' '
    if not sp in line : return line
    while extra_spaces > 0 :
        line = line.replace(sp, sp+' ', extra_spaces)
        extra_spaces = width - len(line)
        sp += ' '
    return line

def formatted_print(text, width=70, align = False):
    para = text.split('\n')
    to_print = ''
    for p in para:
        words = p.split()
        line = ''
        while len(words) > 0 :
            while len(words) > 0 and len(line + words[0]) < width :
                line = ' '.join([line, words.pop(0)]).strip()
            if align and len(words) > 0:
                line = align_text(line, width)
            to_print += line + '\n'
            line = ''
    return to_print

while True:
    text = input('κείμενο')
    if text == '': break
    width = int(input('πλάτος:'))
    print(formatted_print(text, width, True))

#test

st = '''Ούτως ωμίλησεν ο παπα-Φραγκούλης ο Σακελλάριος, αφού έκαμε την ευχαριστίαν του εξ οσπρίων και ελαιών οικογενειακού δείπνου, την εσπέραν της 23ης Δεκεμβρίου του έτους 186… Παρόντες ήσαν, πλην της παπαδιάς, των δυο αγάμων θυγατέρων και του δωδεκαετούς υιού, ο γείτονας ο Πανάγος ο μαραγκός, πεντηκοντούτης, οικογενειάρχης, αναβάς διά να είπη μίαν καλησπέραν και να πιή μίαν ρακιά, κατά το σύνηθες, εις το παπαδόσπιτο• κι η θειά το Μαλαμώ η Καναλάκαινα, μεμακρυσμένη συγγενής, ελθούσα διά να φέρη την προσφοράν της, χήρα εξηκοντούτις, ευλαβής, πρόθυμος να τρέχη εις όλας τάς λειτουργίας και να υπηρετή δωρεάν εις τους ναούς και τα εξωκκλήσια.

«Τ ακούσαμε κι ημείς, παπά» απήντησεν ο γείτονας ο Πανάγος, «έτσ είπανε».

«Τί είπανε; Είναι σίγουρο, σάς λέω» επανέλαβεν ο παπα-Φραγκούλης. «Οι βλοημένοι, δε θα βάλουν ποτέ γνώση. Επήγαν με τέτοιον καιρό να κατεβάσουν ξύλα, απάν απ” του Κουρουπή τα κατσάβραχα, στο Στοιβωτό, εκεί πού δεν μπορεί γίδι να πατήση. Καλά να τα παθαίνουν!»"
'''

print(st)
print('\n formatted text ................')
print(formatted_print(st, 50, True))
