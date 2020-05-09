# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode(val: {self.val}, next: {self.next})'

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1, list2 = [], []
        
        # if not l1 or not l2:
        #     return None
        
        if l1:
            ptr1 = l1
            while ptr1 != None:
                list1.append(ptr1.val)
                # print(n1)
                ptr1 = ptr1.next
        
        if l2:
            ptr2 = l2
            while ptr2 != None:
                list2.append(ptr2.val)
                # print(n1)
                ptr2 = ptr2.next
        
        final_list = sorted(list1 + list2)
        # print(list2)
        
        nodes = [ListNode(x) for x in final_list]
        print(nodes)
        for i in range(1, len(nodes)):
            nodes[i-1].next = nodes[i]
        
        if len(nodes) == 0:
            return None

        return nodes[0]


# if __name__ == '__main__':
#     num1 = []
#     num2 = [0]

#     nodes1 = [ListNode(x) for x in num1]
#     nodes2 = [ListNode(x) for x in num2]

#     for i in range(1, len(nodes1)):
#         nodes1[i-1].next = nodes1[i]

#     for i in range(1, len(nodes2)):
#         nodes2[i-1].next = nodes2[i]

#     sol = Solution()
#     print(sol.mergeTwoLists(None, nodes2[0]))