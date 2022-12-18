# time complexity = O(n)
# space complexity = O(n)

max_data = float("-inf")

def getMaxelement(root) -> int:
    global max_data
    if not root:
        return max_data
    if root.data>max_data:
        max_data = root.data

    getMaxelement(root.left)
    getMaxelement(root.right)
    return max_data

def getMaxElement_NonRecursive(root) -> int:
    if not root:
        return
    stack = []
    result = []
    stack.append(root)

    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right:stack.append(node.right)
        if node.left:stack.append(node.left)