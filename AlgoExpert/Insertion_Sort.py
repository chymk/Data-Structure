'''
Write a function that takes in an array of integers and returns a sorted version of that array.
Use the Insertion Sort algorithm to sort the array.
Sample input: [8, 5, 2, 9, 5, 6, 3]
Sample output: [2, 3, 5, 5, 6, 8, 9]

Algorithm:
To sort an array of size n in ascending order:
1: Iterate from arr[1] to arr[n] over the array.
2: Compare the current element (key) to its predecessor.
3: If the key element is smaller than its predecessor, compare it to the elements before.
Move the greater elements one position up to make space for the swapped element.
'''

def insertion_sort(array):
    for i in range(1,len(array)):
        print(array)
        key = array[i]
        j = i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            array[j] = key
            j -=1
    return array


a=[8, 5, 2, 9, 5, 6, 3]
print(insertion_sort(a))
