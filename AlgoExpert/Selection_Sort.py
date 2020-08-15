'''
Write a function that takes in an array of integers and returns a sorted version of that array.
Use the Selection Sort algorithm to sort the array.
Sample input: [8, 5, 2, 9, 5, 6, 3]
Sample output: [2, 3, 5, 5, 6, 8, 9]
'''

def selection_sort(array):
    for i in range(0,len(array)-2):
        step = i
        for j in range(i,len(array)-1):
            if array[j]<array[j+1]:
                swap(j,j+1,array)

        swap(step,len(array)-1,array)
    return array




def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


a=[8, 5, 2, 9, 5, 6, 3]
print(selection_sort(a))