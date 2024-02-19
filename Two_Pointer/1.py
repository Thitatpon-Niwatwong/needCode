class Solution:
    def isPalindrome(self, s):
        str = "".join(a.lower() for a in s if a.isalnum())
        i = 0
        j = len(str)-1
        for a in range(len(str)):
            if str[i] != str[j]:
                return False
            else:
                i += 1
                j -= 1
        return True


A = Solution()
s = "A man, a plan, a canal: Panama"
print(A.isPalindrome(s))
