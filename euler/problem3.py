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

def removeDupli():
    for x in range(len(nums)-1):
        if nums[x] == nums[x+1]:
            nums.pop(x+1)
            removeDupli()

removeDupli()



for x in range(len(nums)):
    divMax = nums[x] // 2
    print("check Num", nums[x])
    for i in range(divMax):
        if x == 2:
            break
        if i > 1:
            if nums[x] % i == 0:
                print(nums[x], " Is dividable with", i)
                break
        if i == divMax-1:
            print("Higest is ", nums[x])
            exit()
