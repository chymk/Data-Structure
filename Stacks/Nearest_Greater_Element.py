def nearestGrater(A):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]< A[j]:
                temp = A[j]
                A[j] = A[i]
                A[i] = temp
    return A

def nearestGreater(A):
    s = [-1]
    i = 0
    s.append(A[0])
    for i in range(0,len(A)):
        nextNearesGrt = A[i]
        if s[-1]!=-1:
            print("Not Empty")
            element = s.pop()
            while element < nextNearesGrt:
                print(str(element), "-->", str(nextNearesGrt))
                if s[-1] == -1:
                    break
                element = s.pop()
            if element > nextNearesGrt:
                s.append(element)
        s.append(nextNearesGrt)

        while s[-1]!=-1:
            s.pop()
            nextNearesGrt = float('-inf')
            print("Tri")
            print(str(element), "-->", str(nextNearesGrt))

print(nearestGreater([2,1,5,6,2,3]))