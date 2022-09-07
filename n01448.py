from datetime import datetime
import collections


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global ans
        ans = 0

        m = root.val

        def cur_good_Nodes(r, m):
            global ans
            if r is None:
                return
            if r.val >= m:
                ans += 1
                # print(r)
            m_new = max(m, r.val)
            cur_good_Nodes(r.left, m_new)
            cur_good_Nodes(r.right, m_new)
            return

        cur_good_Nodes(root, m)
        return ans


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))