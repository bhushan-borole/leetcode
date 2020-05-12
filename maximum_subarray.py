class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        count = 0
        for i in range(len(nums)):
            count = max(count + nums[i], nums[i])
            res = max(count, res)
        
        return res
        