def nextLargest(num):
    stk = []
    num = str(num)
    str1 = ''
    for i in range(len(num)):
        stk.append(num[i])
    print(stk)

    while stk != []:
        s = stk.pop()
        print(s,' ',str1)
        if len(str1) and int(s) < int(str1[-1]):
            str1 = str1[-1]+"".join(sorted(str1[:-1]+s))
            print("inside if : ",str1)
            while stk != []:
                s = stk.pop()
                str1 = s+str1
            return str1
        else:
            str1 = s + str1
    return -1

# num = 1234986
# print(nextLargest(num))
# print(nextLargest(218765))
# print(nextLargest(4321))