
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # create a hashmap of clones with ids as keys
        # do a dfs and find all the nodes, and clone them
        # do a dfs again and replace all the node links with their clones
        clones = {}

        def get_clone(node):
            if node == None:
                return
            if node.val in clones:
                return clones[node.val]
            clone = Node(node.val,[])
            clones[node.val] = clone
            for nbr in node.neighbors:
                clone.neighbors.append[get_clone(nbr)]

        return get_clone(node)
