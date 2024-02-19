class Solution(object):
    def search(self, nums, target):
        def Find(left, right):
            if left <= right:
                middle = left + (right - left) // 2
                if target == nums[middle]:
                    return middle
                elif target < nums[middle]:
                    return Find(left, middle-1)
                else:
                    return Find(middle+1, right)
            else:
                return -1

        return Find(0, len(nums) - 1)


A = Solution()
nums = [-1, 1]
target = -1
print(A.search(nums, target))
