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
        pi = partQuick(arr,l,r)
        print(l,r)
        quickSort(arr,l,pi-1)
        quickSort(arr,pi+1,r)

def partQuick(arr,start,end):
    p_index= start
    pivot = arr[end]
    for i in range(start,end):
        if arr[i] <= pivot:
            arr[i],arr[p_index] = arr[p_index],arr[i]
            p_index+=1
    arr[p_index],arr[end] = arr[end],arr[p_index]
    return p_index

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i])