from datetime import datetime
import collections


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        global ans
        ans = []

        def sub(r):
            if r == None:
                return
            else:

                sub(r.left)
                ans.append(r.val)
                sub(r.right)

        if root == None: return []
        sub(root.left)
        ans.append(root.val)
        sub(root.right)
        return ans


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()


    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))