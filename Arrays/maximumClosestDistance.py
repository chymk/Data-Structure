def maximumDist(arr):
    n = len(arr)
    l, r = [n] * n, [n] * n

    for i in range(n):
        if arr[i] == 1:
            l[i] = 0
        elif i > 0:
            l[i] = l[i - 1] + 1

    for j in range(n - 1, -1, -1):
        if arr[i] == 1:
            r[i] = 0
        elif i < n - 1:
            r[i] = r[i + 1] + 1
    result = []
    return max(min(l[i], r[i]) for i, x in enumerate(arr) if not x)


print(maximumDist([1, 0, 0, 0, 1, 0, 1]))