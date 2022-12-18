
# calculate total size of tree

class size_of_tree:

    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None

def calculate_total_size(root):
    if not root:
        return 0
    return calculate_total_size(root.left)+calculate_total_size(root.right)+1
# as root is considered as size 1
