def dutchFlagSort(arr):
    low, high = 0,len(arr)-1
    i = 0
    while i <= high:
        print("array ",arr)
        if arr[i] == 0:
            arr[i],arr[low] = arr[low],arr[i]
            print("array {} arr[i]:{}".format(arr,arr[i]))
            i += 1
            low += 1
        elif arr[i] == 1:
            print("array {} arr[i]:{}".format(arr, arr[i]))
            i += 1
        else:
            arr[i],arr[high] = arr[high],arr[i]
            print("array {} arr[i]:{}".format(arr, arr[i]))
            high -= 1
    return  arr

print(dutchFlagSort([0,2,0,1,0,1,2,0,1,1,2]))