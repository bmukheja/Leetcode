# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        stack = [(root, [])]
        output = []
        while stack:
            cur, stack_vals = stack.pop(-1)

            if cur.left == None and cur.right == None:
                output.append("->".join(stack_vals + [str(cur.val)]))
            if cur.right:
                stack.append((cur.right, stack_vals + [str(cur.val)]))
            if cur.left:
                stack.append((cur.left, stack_vals + [str(cur.val)]))
        return output