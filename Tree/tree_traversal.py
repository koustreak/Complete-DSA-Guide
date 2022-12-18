# In order traversal

# LDR and RDL

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder_ldr(root):
    if not root:
        return None

    inorder_ldr(root.left)
    print(root.data,sep='-->',end='-->')
    inorder_ldr(root.right)

def inorder_rdl(root):
    if not root:
        return

    inorder_rdl(root.right)
    print(root.data,sep='-->',end='-->')
    inorder_rdl(root.left)

def preorder_dlr(root):
    if not root:
        return

    print(root.data,sep='-->',end='-->')
    preorder_dlr(root.left)
    preorder_dlr(root.right)


def preorder_drl(root):
    if not root:
        return

    print(root.data, sep='-->', end='-->')
    preorder_dlr(root.right)
    preorder_dlr(root.left)


def postorder_lrd(root):
    if not root:
        return

    preorder_dlr(root.left)
    preorder_dlr(root.right)
    print(root.data, sep='-->', end='-->')

def postorder_rld(root):
    if not root:
        return

    preorder_dlr(root.right)
    preorder_dlr(root.left)
    print(root.data, sep='-->', end='-->')

# Level order traversal

