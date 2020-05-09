from collections import Counter, OrderedDict

class Solution:
    def removeDuplicates(self, nums):
        di = Counter(nums)

        for item in di:
            if di[item] >=2:
                di[item] = 2

        di = OrderedDict(sorted(di.items()))
        sort = []

        for item in di:
            count = di[item]
            for i in range(count):
                sort.append(item)

        for i, n in enumerate(sort):
            nums[i] = n

        return len(sort)



if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    sol = Solution()
    print(sol.removeDuplicates(nums))