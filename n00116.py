from datetime import datetime


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root):
        cur_values = []

        def sub_connect(root, level):
            if level <= len(cur_values):
                root.next = cur_values[level - 1]
                cur_values[level - 1] = root
            else:
                root.next = None
                cur_values.append(root)
            if root.right:
                sub_connect(root.right, level + 1)
            if root.left:
                sub_connect(root.left, level + 1)
        if root:
            sub_connect(root, 1)
        else:
            return None
        return root



if __name__ == "__main__":
    sol = Solution()

    root = Node()
    start_time = datetime.now()
    print(sol.connect([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))