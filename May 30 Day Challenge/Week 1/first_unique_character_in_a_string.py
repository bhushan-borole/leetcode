from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        try:
            di = Counter(list(s))
            count_1 = {k:v for k, v in di.items() if v == 1}
            indexes = [s.index(k) for k in di if di[k] == 1]
            return min(indexes)
        except:
            return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.firstUniqChar('leetcode'))
    print(sol.firstUniqChar('loveleetcode'))