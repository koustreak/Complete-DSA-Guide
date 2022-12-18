#
#
class newnode:
    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None

def inorder(temp):
    if not temp:
        return

    inorder(temp.left)
    print(temp.key,end=" ")
    inorder(temp.right)

def insert(temp,key):

    if not temp:
        root = newnode(key)
        return

    q = []
    q.append(temp)

    while q:
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = newnode(key)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = newnode(key)
            break
        else:
            q.append(temp.right)


if __name__ == '__main__':
    root = newnode(10)
    root.left = newnode(11)
    root.left.left = newnode(7)
    root.right = newnode(9)
    root.right.left = newnode(15)
    root.right.right = newnode(8)

    print("Inorder traversal before insertion:", end=" ")
    inorder(root)

    key = 12
    insert(root, key)

    print()
    print("Inorder traversal after insertion:", end=" ")
    inorder(root)

