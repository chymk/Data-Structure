
def sortColors( nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        count1 = 0
        count2 = 0
        for num in nums:
            if num == 0:
                count0 += 1
            if num == 1:
                count1 += 1
            if num == 2:
                count2 += 1
        sortColors = []
        for i in range(count0):
            sortColors.append(0)
        for i in range(count1):
            sortColors.append(1)
        for i in range(count2):
            sortColors.append(2)

        return sortColors

def sortColors1(nums):
    counter = 0
    is_Sorted = False
    while not is_Sorted:
        is_Sorted = True
        for i in range(0,len(nums)-(counter+1)):
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
                is_Sorted = False
    return nums


print(sortColors1([2,1,0,1,0,0,2,1,2,2,2]))