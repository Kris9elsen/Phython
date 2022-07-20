num = "6,0,0,8,5,1,4,7,5,1,4,3"

numList = num.split(",")

for x in numList:
    print(x)

for x in range(len(numList)-1):
    c = numList[x] + numList[x+1]
    print(c)

for x in range(len(numList)):
    sum = ""
    for i in range(x):
        sum = numList[i]