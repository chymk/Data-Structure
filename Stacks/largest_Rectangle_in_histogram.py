def largestRectangleArea(R):
    maxArea =0
    for i in range(len(R)):
        for j in range(i,len(R)):
            minheight = min(R[i],R[j])

            for k in range(i,j):
                minheight = min(minheight,R[k])

            maxArea = max(maxArea,minheight*(j-i+1))
    return maxArea

def largestRectangleArea1(R):
    maxArea =0
    for i in range(len(R)):
        minheight = R[i]
        for j in range(i,len(R)):
            minheight = min(minheight,R[j])
            maxArea = max(maxArea,(minheight*((j-i)+1)))
    return maxArea

def largestRectangleArea2(height):
    maxArea = 0
    stack = [-1]
    for i in range(len(height)):
        while stack[-1] != -1 and height[stack[-1]] >= height[i]:
            lastElementIndex = stack.pop()
            maxArea = max(maxArea,height[lastElementIndex]*(i-stack[-1]-1))
            print("Stack ->",stack," i ->",i,"maxArea ->",maxArea,"height->",height[i])
        stack.append(i)


    while stack[-1]!= -1:
        print("2nd While")
        lastElementIndex = stack.pop()
        maxArea = max(maxArea, height[lastElementIndex]*(len(height)-stack[-1]-1))
        print("Stack ->", stack, " i ->", i, "maxArea ->", maxArea,"height->",height[i])
        return maxArea

#Time - O(n^3)
#print(largestRectangleArea([2,1,5,6,2,3]))

#Time - O(n^2)
#print(largestRectangleArea1([2,1,5,6,2,3]))

# Time - O(n)
print(largestRectangleArea2([2,1,5,6,2,3]))