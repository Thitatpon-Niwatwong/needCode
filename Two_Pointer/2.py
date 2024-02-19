class Solution(object):
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1
        sorted(numbers)
        for x in range(len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1


A = Solution()
numbers = [2, 7, 11, 15]
target = 9
print(A.twoSum(numbers, target))
