class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        li = sorted(nums1 + nums2)
        even = len(li) % 2 == 0
        mid = int(len(li) / 2)
        if even:
            mid = int(len(li) / 2)
            return (li[mid] + li[mid-1]) / 2
        else:
            return li[mid]
        


# if __name__ == '__main__':
#     sol = Solution()
#     print(sol.findMedianSortedArrays([1, 3], [2]))