from datetime import datetime
import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # global answer
        # answer = copy.deepcopy(root)
        # print(answer)
        def prun_cur_root(r):
            if r is None:
                return None
            r.left = prun_cur_root(r.left)
            r.right = prun_cur_root(r.right)
            if r.val == 0 and r.left == None and r.right == None:
                # print("Вершина вырезана", r)
                # print("answer after cutting", answer)
                return None


            else:
                # print(answer)
                # print(r.val)
                # print(r.left)
                # print(r.right)
                # print("++++++++++")
                return r

        # answer = prun_cur_root(answer)
        # print("=============")
        # print(answer)
        # print("=============")
        return prun_cur_root(root)


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.pruneTree([1,2,3], 4))

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))