def findUniqueSubset(nums):
    nums.sort()
    subset = []
    subset.append([])
    prev = -1
    for num in nums:
        start = 0
        if prev > 0 and num == prev:
            start = end + 1
        end = len(subset)-1
        for j in range(start,end+1):
            set = list(subset[j])
            set.append(num)
            subset.append(set)
        prev = num
    return subset
    
print(findUniqueSubset([1,2,2,3,3]))
