from datetime import datetime
import collections


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        class Solution:
            def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
                global s, count
                ans = []
                s = []
                count = []
                m = root.val

                def cur_averageOfLevels(r, m):

                    global s
                    global count
                    # s = []
                    # count = []
                    m_next = m + 1
                    if r is None:
                        return

                    if m > len(s) - 1:
                        s.append(r.val)
                        count.append(1)
                    else:
                        s[m] += r.val
                        count[m] += 1
                    # print(s, count, m)
                    cur_averageOfLevels(r.left, m_next)
                    cur_averageOfLevels(r.right, m_next)
                    return

                cur_averageOfLevels(root, 0)
                # print(s)
                ans = [s[i] / count[i] for i, _ in enumerate(s)]
                return ans


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))