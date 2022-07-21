def isPalindromic(x):
    str1 = str(x)
    str2 = str1[::-1]
    if str1 == str2:
        return True
    else: 
        return False

palin = []

for x in range(999, 99, -1):
    for i in range(999, 99, -1):
        num = x * i
        if isPalindromic(num):
            palin.append(num)

palin.sort()
print(palin[len(palin)-1])

