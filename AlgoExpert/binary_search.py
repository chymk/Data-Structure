'''Write a function that takes in a sorted array of integers as well as a target integer.
The function should use the Binary Search algorithm to nd if the target
number is contained in the array and should return its index if it is, otherwise -1.

Sample input: [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33

Sample output: 3'''

def binary_search(array,target):
    return binary_search_helper(array,target,0,len(array)-1)

'''def binary_search_helper(array,target,left,right):
    if(left>right):
        return -1
    middle = int((left+right)/2)
    pottential_match = array[middle]
    if pottential_match == target:
        return middle
    elif target < pottential_match:
        return binary_search_helper(array, target, left, middle-1)
    else:
        return binary_search_helper(array,target,middle+1,right)
'''

def binary_search_helper(array,target,left,right):
    while left<=right:
        middle = (left+right)//2
        pottential_match = array[middle]
        #print(pottential_match)
        if target == pottential_match:
            return middle
        elif target < pottential_match:
            right = middle-1
        else:
            left = middle+1
    return -1


print(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73],61))