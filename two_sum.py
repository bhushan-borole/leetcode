# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        if len(nums) == 2:
            return [0, 1]
        di = {}
        for idx, elem in enumerate(nums):
            diff = target - elem
            if diff in di:
                return [di[diff], idx]
            else:
                di[elem] = idx

# Uncomment the below lines if running locally

# if __name__ == '__main__':
#     nums = [2, 7, 11, 15]
#     target = 9
#     sol = Solution()
#     print(sol.twoSum(nums, target))