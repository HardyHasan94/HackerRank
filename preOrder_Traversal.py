# function to print nodes of binary tree in preorder 

def preOrder(root):
    if root:
        print(root.info, end = ' ')
        preOrder(root.left)
        preOrder(root.right)