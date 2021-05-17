# A = -123
# x = str(abs(A))
# if A<0:
#     print("-",end="")
# for i in range(len(x)-1,-1,-1):
#     print(x[i],end="")

# a = [1,None,3,None,None]
# y = 1
# for i in range(len(a)):
#     if a[i] is not None:
#         y = a[i]
#     else:
#         a[i]=y
# print(a)

# String is a palindrome or not



# def isPalindrome(s):
#     return s == s[::-1]
#
# input = "eye"
# print(isPalindrome(input))
# print(isPalindrome("Helicopter"))

#st = "eyhye"
# with characters of a string check if we can make a palindrome or not

#
# def isPalindrome(s,l,h):
#     while l<h:
#
#         if s[l] != s[h]:
#             return False
#         l+=1
#         h-=1
# def palindromeRemoveOneChar(s):
#     l,h = 0,len(s)-1
#     while l<h:
#         if s[l] == s[h]:
#             l+=1
#             h-=1
#         else:
#             if isPalindrome(s,l+1,h):
#                 return l
#             #if isPalindrome(s,l,h-1):
#             #   return h
#             return -1
#     return -2
#
#
#
# flag = palindromeRemoveOneChar("eayye")
# if flag == -1:
#     print("Palindrome can't be formed")
# elif flag == -2:
#     print("It is a palindrome")
# else:
#     print("Palindrome can be formed")

# DNS - ameican_cancer_society
#
# @app.route('/employee',method=['GET'])
# def getEmployee():
#     return data