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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        global ans
        ans = None

        def dfs(root, left_max, right_max):
            global ans
            if root == None:
                ans = 1
                return 0
            if root.left == None and root.right == None:
                if ans == None:
                    ans = 1
                return [root.val, 1]
            else:
                if root.left != None:
                    left_max = dfs(root.left, [None, None], [None, None])
                if root.right != None:
                    right_max = dfs(root.right, [None, None], [None, None])

                # begin again
                if root.val != left_max[0] and root.val != right_max[0]:
                    return [root.val, 1]

                # from left to right
                elif left_max[0] == root.val == right_max[0]:
                    ans = max(ans, left_max[1] + right_max[1] + 1)
                    return [root.val, max(left_max[1], right_max[1]) + 1]

                # if continue from left
                elif left_max[0] == root.val:
                    ans = max(ans, left_max[1] + 1)
                    return [root.val, left_max[1] + 1]

                # if continue from right
                elif right_max[0] == root.val:
                    ans = max(ans, right_max[1] + 1)
                    return [root.val, right_max[1] + 1]

        _ = dfs(root, [None, None], [None, None])
        return ans - 1


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