def is_Sorted(A):
    if len(A) == 1:
        return True
    return A[0]<=A[1] and is_Sorted(A[1:])

A=[1,2,3,4,5,6,7,8,9]
print(is_Sorted(A))