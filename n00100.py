# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p, q):
            if p == None:
                if q == None:
                    return True
                else:
                    return False
            elif q == None:
                return False
            if p.val != q.val: return False
            if p.left == None and q.left != None or p.left != None and q.left == None: return False
            if p.right == None and q.right != None or p.right != None and q.right == None: return False
            ans = True
            if p.left == None and q.left == None:
                pass
            else:
                ans = ans and dfs(p.left, q.left)

            if p.right == None and q.right == None:
                pass
            else:
                ans = ans and dfs(p.right, q.right)

            return ans

        return dfs(p, q)