
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

def Exponential_Search(arr,x):
    if arr[0]==x:
        return 0
    exp=1
    while arr[min(exp,len(arr)-1)]<x:
        exp *=2

    return binary_Search_Iterate(arr,exp//2,exp,x)

arr = [1,2,3,4,5,6,7,8,9]
print(Exponential_Search(arr,9))