class Solution:
    def solve(self, A, B):
        sum1,sum2= 0,0
        sum1 = sum(A)
        i,j = 0,len(A)-B-1
        for k in range(i,j+1):
            sum2 +=A[k]
        min1 =sum2
        i+=1
        j+=1
        while j< len(A):
            sum2+=(A[j]-A[i-1])
            min1 = min(sum2,min1)
            i+=1
            j+=1
        return sum1-min1




s = Solution()
print(s.solve([2, 5, 3 , 1, -2],3))