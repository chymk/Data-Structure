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

uniqueSubString("abbbb")
uniqueSubString("aabccbb")
uniqueSubString("abccde")