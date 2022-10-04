from datetime import datetime
import collections


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:


        global ans
        ans = 0

        s = 0

        def dfs(root, number):
            global ans
            cur_number = 10 * number + root.val
            if root.left == None and root.right == None:
                ans += cur_number
                return
            else:
                if root.left != None:
                    dfs(root.left, cur_number)
                if root.right != None:
                    dfs(root.right, cur_number)
                return
        dfs(root, 0)
        return ans


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.sumNumbers([100,200],150))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
