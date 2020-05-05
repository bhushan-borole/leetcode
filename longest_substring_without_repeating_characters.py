# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        ans, i, j = 0, 0, 0
        
        while i < len(s) and j < len(s):
            if s[j] not in check:
                check.add(s[j])
                j += 1
                ans = max(ans,  j - i)
            else:
                check.remove(s[i])
                i += 1
        
        return ans
        
# Uncomment the below lines if running locally

# if __name__ == '__main__':
#     s = 'abcabcbb'
#     sol = Solution()
#     print(sol.lengthOfLongestSubstring(s))