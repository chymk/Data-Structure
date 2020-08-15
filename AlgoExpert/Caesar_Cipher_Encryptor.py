'''
Given a non-empty string of lowercase letters and a non-negative integer value representing a key,
write a function that returns a new string obtained by shifting every letter in the input string
by k positions in the alphabet, where k is the key. Note that letters should "wrap" around the alphabet;
in other words, the letter "z"
shifted by 1 returns the letter "a".

Sample input:"xyz", 2
Sample output:"zab"
'''


def algo1(str,shift):
    char = list(str)
    ccE = []
    for c in char:
        ccE.append(shiftChar(c,shift))
    return "".join(ccE)


def shiftChar(c,shift):
    asciValue = ord(c)+shift
    if asciValue<=122:
        return chr(asciValue)
    else:
        return chr(96 + (asciValue%122))

def algo2(str,shift):
    alpha = [chr(c) for c in range(97,123)]
    ccE = []
    for s in str:
        ccE.append(getNewLetter(alpha,shift,s))
    return "".join(ccE)

def getNewLetter(alpha,shift,s):
    alphaLoc = alpha.index(s)+shift
    return alpha[alphaLoc] if alphaLoc<=25 else alpha[alphaLoc%26]


print(algo1("xyz", 2))

print(algo2("xyzabpqlmawstu", 3))
