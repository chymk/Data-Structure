'''
Given a non-empty string of lowercase letters and a non-negative integer value representing a key,
write a function that returns a new string obtained by shifting every letter in the input string
by k positions in the alphabet, where k is the key. Note that letters should "wrap" around the alphabet;
in other words, the letter "z"
shifted by 1 returns the letter "a".

Sample input:"xyz", 2
Sample output:"zab"
'''


def caesarCipherEncryptor(str,shift):
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

print(caesarCipherEncryptor("xyz", 2))
