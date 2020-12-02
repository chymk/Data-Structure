'''Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the
target sum, the function should return them in an array, in sorted order. If no two numbers sum up to the target sum, the function should return an empty array.
Assume that there will be at most one pair of numbers summing up to the target sum.

`Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10
Sample output: [-1, 11]'''

def twoNoSumsol1(array,targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1,len(array)):
            secondNum  = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]

    return []

def twoNoSumsol2(array, targetSum):
    for firstNum in array:
        if targetSum-firstNum in array:
            return [firstNum, targetSum-firstNum]
    return []

def twoNoSumsol3(array, targetSum):
    array.sort()
    left = 0
    right = len(array)-1
    while left < right:
        currentSum = array[left] + array[right]
        #print("left :", array[left], " right :", array[right]," sum :",currentSum)
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left+=1
        elif currentSum > targetSum:
            right-=1
    return []


arr = [1,2,3,4,10,11,14,17,20,21,5,6,7,9]
tar = 11

#print(twoNoSumsol1(arr,tar))
#print(twoNoSumsol2(arr,tar))
print(twoNoSumsol3(arr,tar))

