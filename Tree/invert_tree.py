# invert a binary tree

def invert_tree(root):
    if root is None:
        return root
    if root.left or root.right:
        root.left,root.right = root.right,root.left

    root.left = invert_tree(root.left)
    root.right = invert_tree(root.right)