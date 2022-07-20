num = "6,0,0,8,5,1,4,7,5,1,4,3"
numList = num.split(",")

nums = []

for x in range(len(numList)):
    for i in range(len(numList)):
        n = ""
        h = i
        for y in range(x):
            n += numList[h]
            h += 1
            if (len(n) == x):
                n = int(n)
                nums.append(n)
            if (h > len(numList)-1):
                break
nums.sort(reverse = True)
print(nums)
