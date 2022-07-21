flag = False
num = 20
while flag != True:
    sum = 0
    for x in range(1, 20):
        if (num % x) == 0:
            sum += 1
        if sum == 20:
            flag = True
            print(num)
    num += 20