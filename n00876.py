
from datetime import datetime



class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return head
        cur = head
        k = 1
        while cur.next:
            cur = cur.next
            k += 1
        k = k // 2
        cur = head
        while  k > 0:
            cur
            k -= 1
            cur = cur.next
        return cur


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.middleNode([1,2,1,2,3,4,3,2,3],2))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))