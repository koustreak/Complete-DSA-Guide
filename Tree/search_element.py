class newNode():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def ifExists(root,key):
    if not root:
        return False

    if root.data == key:
        return True

    left_found = ifExists(root.left,key)
    if left_found:
        return True

    right_found = ifExists(root.right,key)
    return right_found


if __name__ == '__main__':
    root = newNode(0)
    root.left = newNode(1)
    root.left.left = newNode(3)
    root.left.left.left = newNode(7)
    root.left.right = newNode(4)
    root.left.right.left = newNode(8)
    root.left.right.right = newNode(9)
    root.right = newNode(2)
    root.right.left = newNode(5)
    root.right.right = newNode(6)

    key = 4

    if (ifExists(root, key)):
        print("YES")
    else:
        print("NO")