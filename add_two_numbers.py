# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'ListNode(val: {self.val}, next: {self.next})'

class Solution:
    def addTwoNumbers(self, l1, l2):
        n1, n2 = '', ''

        ptr1 = l1
        while ptr1 != None:
            n1 = n1 + str(ptr1.val)
            print(n1)
            ptr1 = ptr1.next

        ptr2 = l2
        while ptr2 != None:
            n2 = n2 + str(ptr2.val)
            ptr2 = ptr2.next

        n1 = int(n1[::-1])
        n2 = int(n2[::-1])
        add = str(n1 + n2)[::-1]

        nodes = [ListNode(int(x)) for x in add]

        for i in range(1, len(nodes)):
            nodes[i-1].next = nodes[i]

        return nodes[0]

# Uncomment the below lines if running locally

# if __name__ == '__main__':
#     num1 = [2, 4, 3]
#     num2 = [5, 6, 4]

#     nodes1 = [ListNode(x) for x in num1]
#     nodes2 = [ListNode(x) for x in num2]

#     for i in range(1, len(nodes1)):
#         nodes1[i-1].next = nodes1[i]

#     for i in range(1, len(nodes2)):
#         nodes2[i-1].next = nodes2[i]

#     sol = Solution()
#     print(sol.addTwoNumbers(nodes1[0], nodes2[0]))
