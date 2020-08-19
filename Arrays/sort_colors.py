
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

print(sortColors([2,1,0,1,0,0,2,1,2,2,2]))