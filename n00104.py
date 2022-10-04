from datetime import datetime
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def maxDepth(self, root) -> int:
        global ans
        ans = 0

        def dfs(root, depth):
            global ans
            depth += 1
            if root == None:
                ans = 0
                return
            if root.left == None and root.right == None:
                if ans < depth:
                    ans = depth
                    return
            else:
                if root.left != None:
                    dfs(root.left, depth)
                if root.right != None:
                    dfs(root.right, depth)

        dfs(root, 0)
        return ans


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    #root = TreeNode(5,TreeNode(4,TreeNode(11,TreeNode(7,None,None), TreeNode(2,None, None)),None),TreeNode(8, TreeNode(13, None, None), TreeNode(4, TreeNode(5,None, None), TreeNode(1, None, None))))
    root1 = TreeNode(10,TreeNode(5,TreeNode(3,TreeNode(3,None,None), TreeNode(-2,None, None)),TreeNode(2,None,TreeNode(1,None,None))),TreeNode(-3, None, TreeNode(11, None, None)))
    root2 = TreeNode(1, TreeNode(2,None, None), TreeNode(3, None, None))

    print(sol.maxDepth(root2))
    #print(sol.maxDepth(root1))
    #print(sol.maxDepth(root))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))