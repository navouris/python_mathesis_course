# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 20. Ανάκτηση δεδομένων από το διαδίκτυο

# Άσκηση 20.1 Ανάκτηση μαθημάτων από ιστοσελίδα eudoxus.gr


import urllib.request
import urllib.error
import re
url = 'https://service.eudoxus.gr/public/departments/courses/3008/2016'
try:
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        char_set = response.headers.get_content_charset()
        html = response.read().decode(char_set)
except urllib.error.HTTPError as e:
    print('Σφάλμα HTTP:', e.code)
except urllib.error.URLError as e:
        print('Αποτυχία σύνδεσης στον server')
        print('Αιτία: ', e.reason)
else:

    html = html.replace("\n", "")
    h2_tags = re.findall(r"<h2\b[^>]*>(.*?)</h2>", html)
    for tag in h2_tags:
        if "Μάθημα" in tag:
            code = re.findall("\[(.*?)\]", tag)
            if len(code)>0: code = code[0]
            else : code = ""
            name = re.findall(r"]:(.*)", tag)
            if len(name)>0: name = name[0]
            else : name = ""
            print(code, name)

