def bubbleSort(arr):
    flag = False
    while not flag:
        flag = True
        i = 0
        while i<len(arr)-1:
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                flag = False
            i+=1


arr = [1,7,3,9,5,2,6,4]
bubbleSort(arr)
print(arr)