class Solution:
    def myAtoi(self, s):
        valid = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.']
        s = s.strip()
        s = s.replace('+', '')
        if not s or s[0] not in valid or s == '-':
            return 0
        # elif s[0] == '+':
        #     s = s[1:]
        if '+-' in s or '-+' in s:
            return 0
        else:
            neg = False
            if s[0] == '-':
                neg = True
            num = ''
            for i in s:
                if i in valid and i != '-':
                    num += i
                else:
                    break
            # print(num)
            val = int(float(num))
            if neg:
                val = -val

            if val > 2**31 - 1:
                return 2**31 - 1
            elif val < -2**31:
                return -2**31
        # return -val if neg else val
        return val

if __name__ == '__main__':
    sol = Solution()
    # print(sol.myAtoi('-42'))
    print(sol.myAtoi('4304   ibri'))
    print(sol.myAtoi('  -42'))
    print(sol.myAtoi('  -0012a42'))


