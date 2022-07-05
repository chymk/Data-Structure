def selectionSort(arr):
    for i in range(len(arr)):
        minIdx = i
        for j in range(i+1,len(arr)):
            if arr[minIdx]>arr[j]:
                minIdx = j
        arr[i],arr[minIdx] = arr[minIdx],arr[i]

arr = [1,7,3,9,5,2,6,4]
selectionSort(arr)
print(arr)