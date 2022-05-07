# https://leetcode.com/problems/trim-a-binary-search-tree/

class node:
    def __init__(self, val=0, left_=None, right_=None):
        self.data = val
        self.left = left_
        self.right = right_

class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, value, current_node):
        if value < current_node.data:
            if current_node.left == None:
                current_node.left = node(value)
            else:
                self._insert(value, current_node.left)
        else:
            if current_node.right == None:
                current_node.right = node(value)
            else:
                self._insert(value, current_node.right)

    def array_to_bst(self, nums):
        if not nums:
            return None

        mid = len(nums)//2

        node_ = node(nums[mid])

        if self.root == None:
            self.root = node_

            self.root.left = self.array_to_bst(nums[:mid])
            self.root.right = self.array_to_bst(nums[mid+1:])
        else:
            node_.left = self.array_to_bst(nums[:mid])
            node_.right = self.array_to_bst(nums[mid+1:])
            
        return node_


    def insert_level_order(self, nodes, i):
        node_ = node(nums[i])

        node_.left = self.insert_level_order(nodes, 2*i+1)
        node_.right = self.insert_level_order(nodes, 2*i+2)

        return node_

    def in_order(self, curr_node):
        if curr_node != None:
            self.in_order(curr_node.left)
            print(curr_node.data, end = '--')
            self.in_order(curr_node.right)

    def trimBST(self, low, high, current_node):
        if self.root == None:
            return None

        if(current_node.data > high):
            return self.trimBST(low, high, current_node.left)
        if(current_node.data < low):
            return self.trimBST(low, high, current_node.right)

        current_node.left = self.trimBST(low, high, current_node.left)
        current_node.right = self.trimBST(low, high, current_node.right)

        return current_node

if __name__ == "__main__":
    nums = [3,0,4,2,1]
    nums2 = [3, 2, 5, 1, 3, None, 6]

    tree = binary_search_tree()
    tree2 = binary_search_tree()

    for num in nums:
        tree.insert(num)

    tree2.array_to_bst(nums2)

    tree.in_order(tree2.root)
    print('\n',tree2.root.data)

    tree2.trimBST