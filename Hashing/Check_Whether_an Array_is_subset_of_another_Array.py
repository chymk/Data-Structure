def isSubset(arr1,arr2,m,n):
    s = set()

    for item in arr1:
        s.add(item)

    for item in arr2:
        if item in s:
            continue
        else:
            return False
    return True

arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]

m = len(arr1)
n = len(arr2)
if isSubset(arr1, arr2, m, n) == True:
    print("arr2 is subset of arr1 ")
else:
    print("arr2 is not a subset of arr1 ")