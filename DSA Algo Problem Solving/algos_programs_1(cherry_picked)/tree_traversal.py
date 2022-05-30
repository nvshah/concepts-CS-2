from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    post = []

    def dfs(n):
        if not n: return 
        # 1. Left Child 
        dfs(n.left)
        # 2. Right Child 
        dfs(n.right)
        # 3. Current Node 
        post.append(n.val)

    dfs(root)
    return post

def inorderTraversal1(root: Optional[TreeNode]) -> List[int]:
    '''Recursively'''
    res = []
    def inorder(node):
        if not node:
            return
        # 1. Left Child 
        inorder(node.left)
        # 2. Curr Node 
        res.append(node.val)
        # 3. Right Child 
        inorder(node.right)
    #initiate the traversal
    inorder(root)
    return res

def inorderTraversal2(root: Optional[TreeNode]) -> List[int]:
    '''Stack + Iterative Manner'''
    res = []
    curr = root  # pointer to current node
    stack = []   # stack to keep track of node at upper levels

    while curr or stack:  # till any node exists
        # 1. Explore the Depth First Left Most
        while curr:
            stack.append(curr)
            curr = curr.left
        # 2. Add the Top-most elem on stack to {res}
        top = stack.pop()
        res.append(top.val)
        # 3. Explore the Right Part for {top}
        curr = top.right

    return res
