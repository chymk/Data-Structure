def removeDuplicate(Array):
    stkPtr =-1
    i=0
    stack=[]
    while i<len(Array):
        if stkPtr==-1 or Array[stkPtr]!=Array[i]:
            stack.append(Array[i])
            stkPtr+=1
            i+=1
        else:
            stkPtr+=1
            i+=1
    return stack

print(removeDuplicate([2,2,1,5,5,6,2,2,3]))