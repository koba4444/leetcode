from datetime import datetime
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeNodeAmended(TreeNode):
    def __init__(self, max_left=None, max_right=None, val=0, left=None, right=None):
        super().__init__(val, left, right)
        self.max_left = max_left
        self.max_right = max_right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        global ans
        ans = None

        def dfs(root, left_max, right_max):
            global ans
            if root.left == None and root.right == None:
                if ans == None:
                    ans = root.val
                elif ans < root.val:
                    ans = root.val
                left_max = 0
                right_max = 0
                return max(root.val, 0)
            else:
                if root.left != None:
                    left_max = dfs(root.left, None, None)
                if root.right != None:
                    right_max = dfs(root.right, None, None)
                a = root.val + (0 if right_max == None else right_max) + (0 if left_max == None else left_max)
                # print("a=", a)
                ans = max(a, ans)
                m = (max(left_max, right_max) if (left_max != None and right_max != None)
                     else (left_max if left_max != None else right_max)
                     )
                return max(m + root.val, root.val, 0)

        _ = dfs(root, None, None)
        return ans


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    #root = TreeNode(5,TreeNode(4,TreeNode(11,TreeNode(7,None,None), TreeNode(2,None, None)),None),TreeNode(8, TreeNode(13, None, None), TreeNode(4, TreeNode(5,None, None), TreeNode(1, None, None))))
    root1 = TreeNode(10,TreeNode(5,TreeNode(3,TreeNode(3,None,None), TreeNode(-2,None, None)),TreeNode(2,None,TreeNode(1,None,None))),TreeNode(-3, None, TreeNode(11, None, None)))
    root2 = TreeNode(1, TreeNode(2,None, None), TreeNode(3, None, None))

    print(sol.maxPathSum(root2))
    #print(sol.maxPathSum(root1))
    #print(sol.maxPathSum(root))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))