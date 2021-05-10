class Solution:
    def coverPoints(self, A, B):
        count = 0
        for i in range(len(A)-1):
            count+=shortestPath(A[i],B[i],A[i+1],B[i+1])
        return count

def shortestPath(x,y,x1,y1):
    dx = abs(x1-x)
    dy = abs(y1-y)
    return max(dx,dy)
