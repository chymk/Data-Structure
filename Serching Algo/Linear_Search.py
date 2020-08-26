# Time Complexity - O(n)
# Space Complexity -O(1)

def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [3,5,1,0,9,4]
x=15
print(linear_search(arr,x))