num = 600851475143

def isPrime(x):
    flag = True
    for i in range(2, x):
        if (x % i) == 0:
            flag = False
    return flag

for i in range(2, (num // 2)):
    if isPrime(i) == True:
        if (num % i) == 0:
            print(i, "Is a prime factor")


