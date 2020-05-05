class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j = list(J)
        s = list(S)
        count = 0
        
        for jewel in j:
            count += S.count(jewel)
        
        return count