def nearestGrater(A):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]< A[j]:
                temp = A[j]
                A[j] = A[i]
                A[i] = temp
    return A

print(nearestGrater([2,1,5,6,2,3]))