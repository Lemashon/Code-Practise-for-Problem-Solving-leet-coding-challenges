'''
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)
'''

class Solution:
    def bstFromPreorder(self,preorder: list[int]) ->TreeNode:
        # Create an empty stack to hold the nodes of the binary search tree
        stack = []
          # Iterate over the values in the preorder traversal
        for value in preorder:
            # Create a new node with the value
            node = TreeNode(value)
            # While the stack is non-empty and the value of the current node is greater than the value of the top node on the stack
            while stack and stack[-1].val < value:
                node.left = stack.pop()
            if stack:
                stack[-1].right=node
            # Push the current node onto the stack
            stack.append(node)
        return stack[0]
            