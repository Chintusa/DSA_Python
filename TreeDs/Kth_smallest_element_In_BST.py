def inorder(root, result):
    if root is not None:
        inorder(root.left, result)
        result.append(root.data)
        inorder(root.right, result)

def kth_smallest(root, k):
    result = []
    inorder(root, result)
    if 0 < k <= len(result):
        return result[k - 1]
    return None
