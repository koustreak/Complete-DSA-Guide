
# inorder traversal
# l - left child
# d - current node
# r - right child

def inorder_ldr(root):
    if not root:
        return
    stack = []
    node = root
    result = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right
    return result

def inorder_rdl(root):
    if not root:
        return
    stack= []
    result = []
    node= root
    while node or stack:
        if node:
            stack.append(node)
            node = node.right
        else:
            node=stack.pop()
            result.append(node.data)
            node=node.left
    return result

def preorder_dlr(root):
    if not root:
        return
    stack = [].append(root)
    result = []
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.left:stack.append(node.left)
        if node.right:stack.append(node.right)

def preorder_drl(root):
    if not root:
        return
    stack = [].append(root)
    result = []
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.left:stack.append(node.right)
        if node.right:stack.append(node.left)
