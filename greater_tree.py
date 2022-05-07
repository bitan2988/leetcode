# https://leetcode.com/problems/convert-bst-to-greater-tree/solution/

# reverse in-order traversal to ensure we visit nodes in a descending order

class node:
    def __init__(self, val=None):
        self.data = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.total = 0

    def insert(self, nums, i):
        if i>=len(nums)-2//2:
            return None

        node_ = node(nums[i])

        if self.root == None:
            self.root = node_

        node_.left = self.insert(nums, 2*i+1)
        node_.right = self.insert(nums, 2*i+2)

        return node_

    def print_in_order(self, curr_node):
        if(self.root == None or curr_node.data == None):
            return None
        
        self.print_in_order(curr_node.left)
        print(curr_node.data, '--')
        self.print_in_order(curr_node.right)

    def greter_tree(self, root):

        if root is not None:
            self.convertBST(root.right)  # final total of right sub_tree
            self.total += root.val       # initialised self.total = 0
            root.val = self.total
            self.convertBST(root.left)   # now iterate for left part
        return root

    def greter_tree_iterative(self, root):
    # One way to describe the iterative stack method is in terms of the intuitive recursive solution. 
    # First, we initialize an empty stack and set the current node to the root. 
    # Then, so long as there are unvisited nodes in the stack or node does not point to null, 
    # we push all of the nodes along the path to the rightmost leaf onto the stack. 
    # This is equivalent to always processing the right subtree first in the recursive solution, 
    # and is crucial for the guarantee of visiting nodes in order of decreasing value. 
    # Next, we visit the node on the top of our stack, and consider its left subtree. 
    # This is just like visiting the current node before recursing on the left subtree in the recursive solution. 
    # Eventually, our stack is empty and node points to the left null child of the tree's minimum value node, so the loop terminates.
        total = 0
        
        node = root
        stack = []
        while stack or node is not None:
        # push all nodes up to (and including) this subtree's maximum on the stack.
            while node is not None:
                stack.append(node)
                node = node.right

        # now we have reached the end of the tree 
            node = stack.pop()
            total += node.val  #
            node.val = total

        # all nodes with values between the current and its parent lie in the left subtree.
            node = node.left

        return root

if __name__ == "__main__":
    nums = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
    tree1 = BST()

    tree1.insert(nums, 0)
    print(tree1.root.right.data)