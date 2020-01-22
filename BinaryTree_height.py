# This function returns the height of a binary tree

def height(root):
    paths = []
    if root.left:
        paths.append(1+height(root.left))
    if root.right:
        paths.append(1+height(root.right))
    if root.left == None and root.right == None:
        paths.append(0)
    return max(paths)