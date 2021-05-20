class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return None
        li = []
        ptr = head
        while ptr.next != None:
            li.append(ptr.val)
            ptr = ptr.next
        li.append(ptr.val)
        k %= len(li)
        op = li[-k:] + li[:-k]
        print(op)
        op = [ListNode(x) for x in op]
        for i in range(1, len(op)):
            op[i-1].next = op[i]

        if len(op) == 0:
            return None
        return op[0]