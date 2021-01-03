def smallestSubArray(arr,sum):
    windowStart, windowSum, minLength = 0,0,float('inf')
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        while windowSum >= sum:
            minLength = min(minLength,windowEnd-windowStart+1)
            windowSum -= arr[windowStart]
            windowStart += 1
    if minLength == float('inf'):
            return 0
    return minLength

print(smallestSubArray([2, 1, 5, 2, 3, 2],7))
print(smallestSubArray([2, 1, 5, 2, 8],7))
print(smallestSubArray([3,4,1,1,6],8))