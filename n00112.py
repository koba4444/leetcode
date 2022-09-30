from datetime import datetime
import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        global ans
        ans = False

        s = 0

        def dfs(root, target, s):
            global ans
            s += root.val
            if root.left == None and root.right == None:
                if s == target:
                    return True
                else:
                    return False

                return
            else:
                if root.left != None:
                    if dfs(root.left, target, s): return True
                if root.right != None:
                    if dfs(root.right, target, s): return True
                s -= root.val
                # print(root.val, s)
                return False
        if root == None: return False
        ans = dfs(root, targetSum, s)
        return ans


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.pathSum([100,200],150))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))