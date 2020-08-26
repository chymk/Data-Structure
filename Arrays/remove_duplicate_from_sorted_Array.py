def remove_duplicates(nums):
    prevValue = -1000
    arra = []
    for i in range(0,len(nums)-1):
        if nums[i] == prevValue:
            continue
        else:
            arra.append(nums[i])
            prevValue = nums[i]
    return arra

print(remove_duplicates([0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]))