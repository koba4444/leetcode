# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        global valCounter
        global ans
        valCounter = [0] * 9
        ans = 0

        def checkParity():
            global valCounter
            global ans
            res = 0
            for c in valCounter:
                res += c % 2
            if res > 1:
                return 0
            else:
                return 1

        def dfs(root):
            global valCounter
            global ans
            valCounter[root.val - 1] += 1
            if root.left == None and root.right == None:
                ans += checkParity()
            else:
                if root.left != None:
                    dfs(root.left)
                if root.right != None:
                    dfs(root.right)
            valCounter[root.val - 1] -= 1

        dfs(root)
        return ans
