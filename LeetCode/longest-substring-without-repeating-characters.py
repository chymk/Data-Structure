class Solution:
    def lengthOfLongestSubstring(self, str):
        s = set()
        start = 0
        end = 0
        MaxLength = 0
        #print(str," Length ",len(str))

        while start < len(str) - 1 and end < len(str):
            c = str[int(end)]
            if c not in s:
                s.add(c)
                end = end + 1
                #print("Inside if ", s)
            else:

                s.remove(str[start:start + 1])
                #print("Inside Else Remove ", c)

                s.add(c)
                #print("After Add ", s)
                start = start + 1
                end = end + 1
            MaxLength = max(len(s), MaxLength)
            #print(start,end)
            #print("MaxLength ", MaxLength)
        return MaxLength









s = Solution()

print("abcabcde  Length of substring - ",s.lengthOfLongestSubstring("abcabcde"))

print("bbbbbb  Length of substring - ",s.lengthOfLongestSubstring("bbbbbb"))

print("pwwkew  Length of substring - ",s.lengthOfLongestSubstring("pwwkew"))
