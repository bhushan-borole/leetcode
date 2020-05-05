from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)

        for k, v in r.items():
            if k in m and v <= m[k]:
                continue
            else:
                return False

        return True
