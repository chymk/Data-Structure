'''Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ). 
The digits are stored such that the most significant digit is first element of array.'''

def plusOne(A):
    k,carry = len(A)-1,0
    A[k] = (A[k]+1) + carry 
    carry = A[k]//10
    A[k] = A[k]%10
    k-=1
    while carry>0 and k>=0:
        A[k] = A[k] + carry
        carry = A[k]//10
        A[k] = A[k]%10
        k-=1
    if carry==1:
        A.insert(0,1)
    return A
print(plusOne([1,2,3,4]))
