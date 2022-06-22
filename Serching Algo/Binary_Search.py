def binary_search(arr,l,r,target):
    if r>=l:
        mid = l+(r-l)//2
        if target == arr[mid]:
            return mid
        if target > arr[mid]:
            return binary_search(arr,mid+1,r,target)
        else:
            return binary_search(arr,l,mid-1,target)
    return -1


''' Time cOmplexity - O(logn)
Space Complexity - O(logn)'''

#Non Recursive approach

def binary_search_non_Recursive(arr,l,r,target):
    while l<=r:
        mid = l+(r-l)//2
        if target == arr[mid]:
            return mid
        if target < arr[mid]:
            r = mid -1
        else:
            l = mid +1
    return -1


arr= [1,3,5,7,21,54,124,126]
print(binary_search_non_Recursive(arr,0,(len(arr)-1),124))
