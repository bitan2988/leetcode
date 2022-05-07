
# https://leetcode.com/problems/increasing-order-search-tree/submissions/



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if(root is None):
            return root
        
        res = []
        self.inorder(root, res)
        
        root.val = res[0]
        curr_node = root
        
        for i in range(1, len(res)):
            curr_node.left = None
            curr_node.right = TreeNode(res[i])
            curr_node = curr_node.right
                       
        return root
        
    def inorder(self, curr_node, res):
        if curr_node is None:
            return None
        if(curr_node.left):
            self.inorder(curr_node.left, res)
            
        res.append(curr_node.val)
        
        if(curr_node.right):
            self.inorder(curr_node.right, res)
        