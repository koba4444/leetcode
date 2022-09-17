from datetime import datetime
import collections


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head, k):
        global ind_left, ind_right, val_left, val_right, i
        i = 1
        ind_left = 1
        ind_right = None
        val_left = None
        val_right = None
        def is_k_from_end(root, k):
            global ind_left, ind_right, val_left, val_right, i

            if i == k:
                val_left = root.val
                if val_right != None: root.val = val_right

            if root.next == None:
                ind_right = 1
            else:
                i += 1
                if ind_left < k: ind_left += 1
                is_k_from_end(root.next, k)


            if k == ind_right:
                val_right = root.val
                root.val = val_left

            if i == k:
                if val_right != None: root.val = val_right

            if ind_right != None: ind_right += 1
            i -= 1


        def set_valright(root, k, i):
            if i == k:
                root.val = val_right
            else:
                set_valright(root.next, k, i+1)






        is_k_from_end(head, k)
        set_valright(head, k, 1)
        a = 1
        return head

if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    head = ListNode(100,ListNode(90, None))
    print(sol.swapNodes(head, 2))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))