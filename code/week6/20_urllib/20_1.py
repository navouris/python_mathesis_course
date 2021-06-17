# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 20. Ανάκτηση δεδομένων από το διαδίκτυο

#

import urllib.request
import urllib.error
import socket 
# timeout : χρόνος αναμονής σε δευτερόλεπτα
timeout = 10
socket.setdefaulttimeout(timeout) 
# Η κλήση στο urllib.request.urlopen χρησιμοποιεί το timeout
# που ορίστηκε στη βιβλιοθήκη socket
 
req = urllib.request.Request('https://www.upatras.gr/el')
try: 
    with urllib.request.urlopen(req) as response:
        char_set = response.headers.get_content_charset()
        html = response.read().decode(char_set)
    with open("www_upatras_gr.html", "w", encoding = char_set) as p:
        p.write(html)
except urllib.error.HTTPError as e:
    print('Σφάλμα HTTP:', e.code)
except urllib.error.URLError as e:
    print('Αποτυχία σύνδεσης στον server')
    print('Αιτία: ', e)
else:
    print('Φορτώθηκε επιτυχώς η σελίδα')

