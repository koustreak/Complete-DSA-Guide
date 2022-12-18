min_element = float("inf")

def find_min_element(root):
    global min_element
    if not root:
        return min_element
    if root.data<min_element:
        min_element=root.data

    find_min_element(root.left)
    find_min_element(root.right)

    return min_element

def find_min_element_non_recursive(root):
    #global min_element
    if not root:
        return
    else:
        stack = []
        node = root
        result = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node=stack.pop()
                result.append(node.data)
                node=node.right

    return min(result)


def find_min_element_non_recursive(root):
    if not root:
        return
    else:
        stack = []
        stack.append(root)
        result = []
        while stack:
            node = stack.pop()
            result.append(node.data)
            if node.left:stack.append(node.left)
            if node.right:stack.append(node.right)


