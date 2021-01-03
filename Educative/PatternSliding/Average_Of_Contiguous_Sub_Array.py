def averageOfContiguosSubArray(arr,k):
    n = len(arr) - k + 1
    avg = []
    for i in range(n):
        avg.append(sum(arr[i:k+i])/k)
    print(avg)

averageOfContiguosSubArray([1, 3, 2, 6, -1, 4, 1, 8, 2],5)
