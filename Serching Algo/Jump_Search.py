import math

def Jump_Search(arr, x,n):
    step = int(math.sqrt(x))
    prev = 0
    while arr[int(min(step,len(arr)-1))]<x:
        prev = step
        step += int(math.sqrt(n))
        if step >= n-1:
            step = min(n-1,step)
        #print("prev: ",prev,"   step: ",step)

    while prev<=step:
        if arr[prev] == x:
            return prev
        prev += 1
    return -1

arr = [1,2,3,4,5,6,7,8,9]
print(Jump_Search(arr,5,9))
