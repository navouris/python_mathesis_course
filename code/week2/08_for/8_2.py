# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 8. Δομή for

# Άσκηση 8.2
#Να τυπώσετε διδιάστατη λίστα 3 χ 4

li1 = [1,2,3, 9]
li2 = [5,6,7, 8]
li3 = [0,4,4, 0]
li = [li1,li2,li3]

for i in li:
    for j in i:
        print(j, end ="\t")
    print()

 
