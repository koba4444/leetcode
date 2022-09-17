from datetime import datetime
import collections


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):

        def double_deap_and_swap(root):
            if root == None or root.next == None:
                pass
            else:
                double_deap_and_swap(root.next.next)
                s = root.val
                root.val = root.next.val
                root.next.val = s

        if head == None or head.next == None: return head
        double_deap_and_swap(head)
        return head

if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,None))))
    print(sol.swapPairs(head))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))