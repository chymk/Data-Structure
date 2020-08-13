'''Write a function that takes in an array of integers and returns a sorted version of that array.
Use the Bubble Sort algorithm to sort the array.

Sample input: [8, 5, 2, 9, 5, 6, 3]
Sample output: [2, 3, 5, 5, 6, 8, 9]'''


def bubble_sort(array):
    counter = 0
    is_sorted = False
    while not is_sorted:
        counter = 0
        is_sorted = True
        print(array)
        for j in range(0,len(array)-(counter+1)):
            if array[j]>array[j+1]:
                swap_array_places(array,j,j+1)
                is_sorted=False
            counter += 1
    print("\\")
    return  array

def swap_array_places(array,i,j):
    array[i],array[j] = array[j],array[i]
    return array


arr=[8, -17,5, 2, 9, 5, 6, 3,-1]

print(bubble_sort(arr))