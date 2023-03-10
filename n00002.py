


"""
Too slow. Last 5%.
=========================================
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = result
        zero_node = ListNode(None)
        k = 0
        plus0_1 = 0
        table = list([[[None for c in range(2)] for j in range(10)] for k in range(10)])

        for a in range(10):
            for b in range(10):
                for c in range(2):
                    table[a][b][c] = ((a + b + c) % 10, (a + b + c) // 10)

        plusnew = 0
        cur1 = l1
        cur2 = l2
        while cur1.val is not None or cur2.val is not None:
            val1 = cur1.val or 0
            val2 = cur2.val or 0
            plus0_1 = plusnew
            current.val = table[val1][val2][plus0_1][0]
            plusnew = table[val1][val2][plus0_1][1]
            cur1 = cur1.next or zero_node
            cur2 = cur2.next or zero_node
            if cur1.val is not None or cur2.val is not None or plusnew:
                current.next = ListNode()
                current = current.next
        if plusnew:
            current.val = 1
            current.next = None
        return result
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode()
        current = result
        zero_node = ListNode(None)
        k = 0
        plus0_1 = 0
        table = list([[[None for c in range(2)] for j in range(10)] for k in range(10)])

        for a in range(10):
            for b in range(10):
                for c in range(2):
                    table[a][b][c] = ((a + b + c) % 10, (a + b + c) // 10)

        plusnew = 0
        cur1 = l1
        cur2 = l2
        while cur1.val is not None or cur2.val is not None:
            val1 = cur1.val or 0
            val2 = cur2.val or 0
            plus0_1 = plusnew
            current.val = table[val1][val2][plus0_1][0]
            plusnew = table[val1][val2][plus0_1][1]
            cur1 = cur1.next or zero_node
            cur2 = cur2.next or zero_node
            if cur1.val is not None or cur2.val is not None or plusnew:
                current.next = ListNode()
                current = current.next
        if plusnew:
            current.val = 1
            current.next = None
        return result


l2 = ListNode(7, ListNode(3))
l1 = ListNode(0)
s = Solution()
print(s)
#print(s.addTwoNumbers(l1, l2).val, s.addTwoNumbers(l1, l2).next.val , s.addTwoNumbers(l1, l2).next.next.val, s.addTwoNumbers(l1, l2).next.next.next)
print(s.addTwoNumbers(l1, l2).val, s.addTwoNumbers(l1, l2).next.val)