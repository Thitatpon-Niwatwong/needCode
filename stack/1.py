class Solution:
    def isValid(self, s):
        stack = []
        dic = {'(': ')', '{': '}', '[': ']'}
        for char in s:
            if char in dic.keys():
                stack.append(char)
            elif char in dic.values():
                if not stack or dic[stack.pop()] != char:
                    return False
            else:
                return False
        return not stack


A = Solution()
s = "(())}"
print(A.isValid(s))
