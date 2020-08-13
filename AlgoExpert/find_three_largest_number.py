'''
Write a function that takes in an array of integers and returns a sorted array of the three largest
integers in the input array.Note that the function should return duplicate integers if necessary;
for example, it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].
Sample input: [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
Sample output: [18, 141, 541]
'''

def three_largest_number(array):
    largest_Integer = [None,None,None]
    for num in array:
        updateLargest(largest_Integer, num)
        print(largest_Integer)
    print("")
    return largest_Integer

def updateLargest(largest_Integer, num):
    if largest_Integer[2] is None or num > largest_Integer[2]:
        return shiftLargest(largest_Integer, num, 2)
    elif largest_Integer[1] is None or num > largest_Integer[1]:
        return shiftLargest(largest_Integer,num, 1)
    elif largest_Integer[0] is None or num > largest_Integer[0]:
        return shiftLargest(largest_Integer, num, 0)

def shiftLargest(largest_Integer, num, i):
    for k in range(0,len(largest_Integer)-1):
        if k == i:
            break
        largest_Integer[k] = largest_Integer[k+1]


    largest_Integer[i] = num
    return largest_Integer


arr= [141, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(three_largest_number(arr))
