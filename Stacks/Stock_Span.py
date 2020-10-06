def calculateSpan(price,n, S):
    S[0]=1
    for i in range(1,n,1):

        S[i] = 1
        j = i - 1
        while (j >= 0) and (price[i] >= price[j]):
            S[i] += 1
            j -= 1


def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    # Driver program to test above function


price = [10, 4, 5, 90, 120, 80]
n = len(price)
S = [None] * n

# Fill the span values in list S[]
calculateSpan(price, n, S)

# print the calculated span values
printArray(S, n)