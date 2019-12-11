# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_till_now = 0
        if root:
            stack = [(root,1)]
        else:
            return 0
        while stack:
            node,cur_depth = stack.pop(-1)
            max_till_now = max(max_till_now,cur_depth)
            if node.right:
                stack.append((node.right,cur_depth+1))
            if node.left:
                stack.append((node.left,cur_depth+1))
        return max_till_now