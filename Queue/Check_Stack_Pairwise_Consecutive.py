def checkPairWiseConsecutive(a):
    flag = True
    if len(a)<1:
        print("Stack is empty")
        return False
    ax = []
    while len(a)!=0:
        ax.append(a.pop())
    print("ax : ",ax)
    # Compare consecutive elements
    while len(ax)!=0:
        n = ax.pop()
        a.append(n)
        if len(ax)!=0:
            m = ax.pop()
            a.append(m)
            if abs(m-n)!=1:
                flag = False
                break
    print("a : ",a)
    return flag
s=[4, 5, -2, -3, 11, 10, 5, 6, 20]
print(checkPairWiseConsecutive(s))
