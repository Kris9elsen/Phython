times = input("Enter amount of times to add: ")
times = int(times)
res = 1
i = 0

while i < times:
    print(i + 1, " : ",  res)
    res = res * 2
    i = i + 1