def maximumSum(arr,k):
    Result = 0
    windowStart,windowSum = 0,0.0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k-1:
            Result = max(windowSum,Result)
            windowSum -= arr[windowStart]
            windowStart += 1
    print(Result)

maximumSum([2,1,5,1,3,2],3)
