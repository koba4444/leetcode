from datetime import datetime
import collections


class Solution():
    def mergeTwoLists(self, list1, list2):
        if list1.val == None:
            return list2.val
        else:
            if list2.val == None:
                return list1.val
            else:
                l1 = list1.next
                l2 = list2.next
                list1.next = list2.val
                list2.next = self.mergeTwoLists(list1.next, list2.next)
                return list1.val


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.mergeTwoLists([1,2,4], [1,3,4]))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))