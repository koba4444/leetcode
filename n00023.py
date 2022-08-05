# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from datetime import datetime
#====================================================================================
import copy

class Ordered_roots:
    def __init__(self, els=[]):
        self.els = els

    def insert(self, el):
        self.els.append(el)
        self.els.sort(key=lambda x: x.val, reverse=True)

    def get_min_el(self):
        if len(self.els) == 0: return None, None, None
        y = self.els.pop()
        return y, y.next, y.val


class Solution:
    def mergeKLists(self, lists):
        global last_val
        n = len(lists)
        answer = None
        answer_array = []
        if n == 0: return None
        oroots = Ordered_roots()
        for i, v in enumerate(lists):
            if v != None:
                oroots.insert(ListNode(v.val, v.next))

        while True:
            cur, nnext, val = oroots.get_min_el()

            if val == None:
                i_previouse = answer
                for i in answer_array:
                    i_previouse.next = copy.copy(i)
                    i_previouse = i_previouse.next
                return answer

            if answer == None:
                answer = ListNode()
                answer.val = val
                answer.next = None
            else:
                answer_array.append(cur)
            if nnext != None:
                oroots.insert(nnext)

#============================================================================================

if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    input = [[]]
    a1 = ListNode(1)
    a2 = ListNode(4)
    a3 = ListNode(5)
    a4 = ListNode(1)
    a5 = ListNode(3)
    a6 = ListNode(4)
    a7 = ListNode(2)
    a8 = ListNode(6)

    a1.next = a2
    a2.next = a3
    a4.next = a5
    a5.next = a6
    a7.next = a8

    input = [a1,a4,a7]



    print(sol.mergeKLists(input))
    # print(sol.mergeKLists([[3]]))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))