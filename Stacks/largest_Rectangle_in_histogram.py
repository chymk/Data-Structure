def largestRectangleArea(R):
    maxArea =0
    for i in range(len(R)):
        for j in range(i,len(R)):
            minheight = min(R[i],R[j])

            for k in range(i,j):
                minheight = min(minheight,R[k])

            maxArea = max(maxArea,minheight*(j-i+1))

def largestRectangleArea(R):
    maxArea =0
    for i in range(len(R)):
        minheight = R[i]
        for j in range(i,)


    return maxArea
#Time - O(n^3)
print(largestRectangleArea([2,1,5,6,2,3]))

#Time - O(n^2)

print(largestRectangleArea1([2,1,5,6,2,3]))