# mathesis.cup.gr
# N. Αβούρης: Εισαγωγή στην Python
# Μάθημα 9. Δομή while

# βρες τους 10 μικρότερους πρώτους αριθμούς
primes = []
num = 2
while len(primes) < 10 :
    x = num // 2
    while x > 1 :
        if num % x == 0:
            break
        x -= 1
    else:
        primes.append(num)
    num += 1
print(primes)

    
