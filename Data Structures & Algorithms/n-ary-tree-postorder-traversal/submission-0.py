"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result=[]
        def inorder(root):
            if not root:
                return
            for child in root.children:
                inorder(child)
            result.append(root.val)
        inorder(root)
        return result 