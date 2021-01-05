'''Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".'''
def uniqueSubString(str):
    windowStart, count = 0,0
    q = []
    for windowEnd in range(len(str)):
        if str[windowEnd] not in q:
            q.append(str[windowEnd])
            count = max(count,len(q))
            print(q)
        else:
            q.append(str[windowEnd])
            print(q)
            while len(q) != len(set(q)):
                q.pop(0)
                print("Inside While",q)

    print(count)

def uniqueSubStringOptimize(str):
    windowStart,maxCount = 0,0
    hashMap = {}
    print(str)
    for windowEnd in range(len(str)):
        rightChar = str[windowEnd]

        if rightChar in hashMap:
            windowStart = max(windowStart,hashMap[rightChar]+1)
        hashMap[rightChar] = windowEnd
        maxCount = max(maxCount,windowEnd-windowStart+1)
        print(" rightChar",rightChar," windowStart",windowStart
              , " windowEnd",windowEnd," maxCount",maxCount,"hashmap ",hashMap)
    print(maxCount)

#uniqueSubString("abbbb")
#uniqueSubString("aabccbb")
#uniqueSubString("abccde")

uniqueSubStringOptimize("abbbb")
uniqueSubStringOptimize("aabccbb")
uniqueSubStringOptimize("abccde")