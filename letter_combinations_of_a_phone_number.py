from itertools import product

class Solution:
    def letterCombinations(self, digits):
        if digits == '':
            return []
         
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        if len(digits) == 1:
            return phone[digits]
        
        temp = []
        for d in digits:
            temp.append(phone[d])

        out = product(*temp)
        return [''.join(o) for o in out]


# if __name__ == '__main__':
#     digits = '234'
#     sol = Solution().letterCombinations(digits)
#     print(sol)
