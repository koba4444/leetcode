from datetime import datetime
import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        global ans
        ans = []
        cur_path = []
        s = 0

        def dfs(root, target, s, cur_path):
            global ans
            s += root.val
            cur_path.append(root.val)
            if root.left == None and root.right == None:
                if s == target:
                    ans.append(cur_path.copy())
                    # print("appending", cur_path)
                cur_path.pop()
                return
            else:
                if root.left != None:
                    dfs(root.left, target, s, cur_path)
                if root.right != None:
                    dfs(root.right, target, s, cur_path)
                cur_path.pop()
                s -= root.val
                # print(root.val, s)
                return

        dfs(root, targetSum, s, cur_path)
        return ans


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.pathSum([100,200],150))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))