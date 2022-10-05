from datetime import datetime
import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        def ins(root, val, depth, cur_depth):
            if depth == 1:
                first = TreeNode(val, root, None)
                return first

            if cur_depth == depth:

                if root.left != None:
                    l = TreeNode(val, root.left, None)
                    root.left = l
                    print(cur_depth, "l1")
                else:
                    l = TreeNode(val, None, None)
                    root.left = l
                    print(cur_depth, "l2")

                if root.right != None:
                    r = TreeNode(val, None, root.right)
                    root.right = r
                    print(cur_depth, "r1")
                else:
                    r = TreeNode(val, None, None)
                    root.right = r
                    print(cur_depth, "r2")

                return
            else:
                if root.left != None:
                    ins(root.left, val, depth, cur_depth + 1)
                if root.right != None:
                    ins(root.right, val, depth, cur_depth + 1)

        ans = ins(root, val, depth, 2)
        return ans if ans != None else root


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()
    print(sol.divide(...))
    print(sol.bagOfTokensScore([100,200],150))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))