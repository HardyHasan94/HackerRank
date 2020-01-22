# This code solves the Inorder Traversal problem

def inOrder(root):
    #Write your code here
    if root.left:
        inOrder(root.left)
    print(root.info, end = ' ')
    if root.right:
        inOrder(root.right)
