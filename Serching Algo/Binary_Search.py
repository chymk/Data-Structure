# Time Complexity - O(logn)
# Space Complexity - O(logn)

def binary_Search_Recur(arr,l,r,x):
    mid = (l+r)//2
    if r >= 1:
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return binary_Search_Recur(arr,0,mid-1,x)
        else:
            return binary_Search_Recur(arr, mid+1, r, x)
    else:
        return -1

# Time Complexity - O(logn)
# Space Complexity - O(1)
def binary_Search_Iterate(arr, l, r, x):
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == x:
            return mid
        elif x<arr[mid]:
            r = mid-1
        else:
            l = mid+1
    return -1


arr = [1,2,3,4,5,6,7,8,9]
print(binary_Search_Iterate(arr,0,len(arr)-1,9))
