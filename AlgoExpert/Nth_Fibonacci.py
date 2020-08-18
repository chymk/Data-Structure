'''
The Fibonacci sequence is defined as follows: the 1st number of the sequence is 0, the second number is 1,
and the nth number is the sum of the (n - 1)th and (n - 2)th numbers. Write a function that takes in an
integer n and returns the nth Fibonacci number.

Sample input: 6

Sample output: 5 (0, 1, 1, 2, 3, 5)
'''

def getFibonacci1(num):
    if num == 2:
        return 1
    elif num == 1:
        return 0
    else :
        return getFibonacci1(num-1)+getFibonacci1(num-2)


print(getFibonacci1(8))

