class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set()
        for i in range(0, len(nums)):
            temp = target - nums[i]
            if temp in s:
                return [i, nums.index(temp)]
            s.add(nums[i])

