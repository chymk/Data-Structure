def partition(arr,l,h):
    i = l
    j = h
    while i<j:
        while arr[l]>arr[i]:
            i+=1
        while arr[l]<arr[j]:
            j-=1
            print(arr)
        arr[i],arr[j] = arr[j],arr[i]
    arr[l],arr[j] =arr[j],arr[l]
    print("Return ",arr[j])
    return j

def quickSort(arr,l,r):
    if l<r:
        pi = partition(arr,l,r)
        quickSort(arr,l,pi)
        quickSort(arr,pi+1,r)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i])