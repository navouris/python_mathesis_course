# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 20. Ανάκτηση δεδομένων από το διαδίκτυο

# καλή πρακτική: ορισμός User Agent

import urllib.request
import urllib.error
my_UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
url = 'https://www.google.gr/#q=python&*'
try:
    headers = {}
    headers['User-Agent'] = my_UA
    req = urllib.request.Request(url, headers = headers)
    with urllib.request.urlopen(req) as response:
        char_set = response.headers.get_content_charset()
        html = response.read().decode(char_set)
    with open("www_google_com_q_python.html", "w", encoding = char_set) as p:
        p.write(html)
except urllib.error.HTTPError as e:
    print('Σφάλμα HTTP:', e.code)
except urllib.error.URLError as e:
        print('Αποτυχία σύνδεσης στον server')
        print('Αιτία: ', e.reason)
else:
    print('τέλος προγράμματος')

