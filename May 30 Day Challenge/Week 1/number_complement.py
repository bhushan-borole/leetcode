class Solution:
    def findComplement(self, num: int) -> int:
        bin_str = bin(num)[2:]
        new_str = '1' * len(bin_str)
        return int(new_str, 2) ^ int(bin_str, 2)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findComplement(1))