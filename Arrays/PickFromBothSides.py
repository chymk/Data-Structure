class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        X  = []
        sum = 0
        for i in range(len(A)):
            if i<B or i>(len(A)-1-B):
                X.append(A[i])
        print(X)
        for i in range(len(X)):
            currSum = 0
            j,k = i,0
            print("index:",i," ",i+B,"less than",len(X)-1)
            if i+B < len(X)-1 or i+B>len(X)-B-1:
                while k < B:
                    currSum += X[j]
                    print(X[j])
                    j = (j + 1) % B
                    k += 1
                print(currSum)
                print("---------------------------")
            sum = max(currSum,sum)
        print(sum)




s = Solution()
s.solve([5, -2, 3 , 1, 2],3)