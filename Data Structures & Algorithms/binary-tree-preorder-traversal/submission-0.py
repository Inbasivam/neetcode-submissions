# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):

 
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def traversal(root):
            if not root:
                return
            result.append(root.val)
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        return result