def smallestSubArray(arr,sum):
    maximum = 0
    for i in range(len(arr)):
        if sum in arr:
            return i+1
        else:
            maximum = max(arr)
            if maximum > sum:
                return i+1
            else:
                arr.remove(maximum)
                sum -= maximum

print(smallestSubArray([2, 1, 5, 2, 3, 2],7))
print(smallestSubArray([2, 1, 5, 2, 8],7))
print(smallestSubArray([3,4,1,1,6],8))