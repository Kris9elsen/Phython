while 1 > 0:
    cal = input("Enter math: ")
    chars = cal.split(' ')
    print(chars)

    num1 = int(chars[0])
    num2 = int(chars[2])

    if chars[1] == '+':
        res = num1 + num2

    if chars[1] == '-':
        res = num1 - num2

    if chars[1] == '*':
        res = num1 * num2

    if chars[1] == '/' or chars[1] == ':':
        res = num1 / num2

    print(res)