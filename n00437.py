from datetime import datetime
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import numpy as np
class Solution:
    def pathSum(self, root, targetSum) -> int:
        global ans
        global s
        ans = 0
        s = np.zeros((1001,), dtype=int)
        def dfs(root, target, s, n_start):
            global ans
            for i in range(n_start+1):
                s[i] += root.val
                if s[i] == target:
                    ans += 1
            if root.left == None and root.right == None:
                for i in range(n_start+1):
                    s[i] -= root.val
                return
            else:
                if root.left != None:
                    dfs(root.left, target, s, n_start+1)
                if root.right != None:
                    dfs(root.right, target, s, n_start+1)
                for i in range(n_start+1):
                    s[i] -= root.val
                return

        dfs(root, targetSum, s, 0)
        return ans


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    #root = TreeNode(5,TreeNode(4,TreeNode(11,TreeNode(7,None,None), TreeNode(2,None, None)),None),TreeNode(8, TreeNode(13, None, None), TreeNode(4, TreeNode(5,None, None), TreeNode(1, None, None))))
    root1 = TreeNode(10,TreeNode(5,TreeNode(3,TreeNode(3,None,None), TreeNode(-2,None, None)),TreeNode(2,None,TreeNode(1,None,None))),TreeNode(-3, None, TreeNode(11, None, None)))

    print(sol.pathSum(root1, 8))
    #print(sol.pathSum(root, 22))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))