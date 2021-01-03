'''Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".'''

def longestSubString(str,k):
    windowStart,count = 0,0
    distChar = []
    for windowEnd in range(len(str)+1):
        distChar = str[windowStart:windowEnd]
        distCharLen = len(set(distChar))
        if distCharLen <= k:
            count = max(count, len(distChar))
        else:
            windowStart += 1
        #print("char: ", distChar, " distCharLen:", distCharLen, " count:", count," windowStart:",windowStart," windowEnd:",windowEnd)
    return count

print(longestSubString("araaci",2))
print(longestSubString("araaci",1))
print(longestSubString("cbbebi",3))