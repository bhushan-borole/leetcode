class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sort = sorted(list(set(nums)))
        for i, n in enumerate(sort):
            nums[i] = n
        return len(sort)
