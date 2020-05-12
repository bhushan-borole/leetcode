class Solution:
    def threeSum(self, nums):
        if len(nums)<3:
            return []
        
        if len(nums)==3:
            if sum(nums) == 0:
                return [nums]
            return []
        
        out = []
        N = len(nums) 
        my_dict = {x:[] for x in nums}
        
        for i in range(N):
            my_dict[nums[i]].append(i)

        # print(my_dict)
            
        unique_list = list(set(nums))
        n = len(unique_list)
        
        for i in range(n):
            a = unique_list[i]
            if a == 0 and len(my_dict[a]) >= 3:
                out.append([0, 0, 0])

            elif a != 0 and len(my_dict[a]) >= 2 and -2*a in my_dict:
                out.append([a, a, -2*a])
                
            for j in range(i+1, n):
                b = unique_list[j]
                c = -(a+b)
                if c in my_dict and c > max(a, b):
                    out.append([a, b, c])
        return out

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    sol = Solution().threeSum(nums)
    print(sol)