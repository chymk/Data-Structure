def averageOfContiguousSubArray(arr,k):
    n = len(arr) - k + 1
    avg = []
    for i in range(n):
        avg.append(sum(arr[i:k+i])/k)
    print(avg)

def averageOfContiguousSubArray2(arr,k):
    result = []
    windowStart, windowSum = 0,0.0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k-1:
            result.append(windowSum/k)
            windowSum -= arr[windowStart]
            windowStart += 1
    print(result)

averageOfContiguousSubArray([1, 3, 2, 6, -1, 4, 1, 8, 2],5)
averageOfContiguousSubArray2([1, 3, 2, 6, -1, 4, 1, 8, 2],5)