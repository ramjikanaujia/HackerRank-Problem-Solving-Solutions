


def in_order(root, arr):
    if root.left is not None:
        in_order(root.left, arr)
    arr.append(root.data)
    if root.right is not None:
        in_order(root.right, arr)
    return arr

def check_binary_search_tree_(root):
    tree_in_list = in_order(root, [])
    for i in range(1, len(tree_in_list)):
        if tree_in_list[i] <= tree_in_list[i - 1]:
            return False
    return True