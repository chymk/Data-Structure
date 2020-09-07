def bitStrings(n):
    if n == 0:
        return []
    if n == 1:
        return ['0','1']
    else:
        return appendAtBeginning('0',bitStrings(n-1))+appendAtBeginning('1',bitStrings(n-1))

def appendAtBeginning(x,L):
    return [x + element  for element in L]

print(bitStrings(4))