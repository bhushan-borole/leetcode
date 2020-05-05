# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        if x < 0:
            rev = -int(str(abs(x))[::-1])
        else:
            rev = int(str(x)[::-1])
        
        if rev > 2**31 - 1 or rev < -2**31 - 1:
            return 0
        return rev

# Uncomment the below lines if running locally

# if __name__ == '__main__':
#     n = [123, -123, 120]
#     sol = Solution()
#     print(sol.reverse(n[2]))