def tripletWithSmallerSum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr)-2):
        count += searchPair(arr,target - arr[i],i)
    return count

def searchPair(arr,targetSum, first):
    count = 0
    left, right = first + 1, len(arr)-1
    while left < right:
        if arr[left] + arr[right] < targetSum:
            count += right - left
            left += 1
        else:
            right -= 1
        print("count ", count, " left ", left, " right ", right, " targetSum ", targetSum)
    return count

print(tripletWithSmallerSum( [-1, 4, 2, 1, 3], 5))
print(tripletWithSmallerSum([-1, 0, 2, 3],3 ))
