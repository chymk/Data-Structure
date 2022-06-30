#insertion_sort
def insertionSort(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i-1
        while j>=0 and A[j]>key:
            A[j+1],A[j] = A[j],A[j+1]
            j-=1

arr = [1,7,3,9,5,2,6,4]
insertionSort(arr)
print(arr)