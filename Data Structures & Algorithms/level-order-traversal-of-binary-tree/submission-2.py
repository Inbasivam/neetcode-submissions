# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]

        def level(node,depth):
            if not node:
                return None
            if len(result)==depth:
                result.append([])
            result[depth].append(node.val)
            level(node.left,depth+1)
            level(node.right,depth+1)
        level(root,0)
        return result