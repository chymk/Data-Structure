class Solution:

    def maxset(self, A):
        ans = []
        Sum, maxSum, left, right, aleft, aright = 0, 0, 0, 0, -1, -1
        for i in range(len(A)):
            if A[i] >= 0:
                Sum += A[i]
                if Sum > maxSum or (Sum == maxSum and aright - aleft < right - left):
                    maxSum = Sum
                    aleft = left
                    aright = right
            else:
                left += 1
                Sum = 0
            right += 1
        if aleft == -1:
            return ans
        return A[aleft:aright + 1]

s = Solution()
print(s.maxset([1, 2, 5, -7, 2, 3]))