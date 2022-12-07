class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root, low, high, ans):
            s = 0
            if root.left == None and root.right == None:
                if low <= root.val <= high:
                    return root.val
                else:
                    return ans
            else:

                if root.left != None:
                    s += dfs(root.left, low, high, 0)
                if root.right != None:
                    s += dfs(root.right, low, high, 0)
                if low <= root.val <= high: s += root.val
                return s

        return dfs(root, low, high, 0)