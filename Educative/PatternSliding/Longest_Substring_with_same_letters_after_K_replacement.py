def longestSubstringSameCharAfterReplacement(str,k):
    windowStart,maxCount = 0,0
    hashMap = {}
    for windowEnd in range(len(str)):
        rightChar = str[windowEnd]
        if rightChar not in hashMap:
            hashMap[rightChar] = 0
        hashMap[rightChar] += 1
        while k < len(hashMap):
            leftChar = str[windowStart]
            hashMap[leftChar] -= 1
            if hashMap[leftChar] == 0:
                del hashMap[leftChar]
            windowStart += 1
        maxCount = max(maxCount,windowEnd - windowStart + 1)
    print(maxCount)

longestSubstringSameCharAfterReplacement("aabccbb",2)
longestSubstringSameCharAfterReplacement("abbcb",1)
longestSubstringSameCharAfterReplacement("abccde",1)