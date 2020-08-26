import math

def Jump_Search(arr, x):
    step = math.sqrt(x)
    while(arr[int(min(step,len(arr)))]<x):
