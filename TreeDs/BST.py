class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if not root:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root  

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)

    def getMinNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, root, key):
        if not root:
            return root
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            # Node to be deleted found
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:  
                return root.left
            else:
                # Node with two children
                minNode = self.getMinNode(root.right)
                root.data = minNode.data
                root.right = self.delete(root.right, minNode.data)
        return root

        
bst = BST()
bst.root = bst.insert(bst.root, 10)
bst.root = bst.insert(bst.root, 1)
bst.root = bst.insert(bst.root, 16)
bst.root = bst.insert(bst.root, 20)
bst.root = bst.insert(bst.root, 5)

print("Inorder before deletion:")
bst.inorder(bst.root)
print()

val=16
bst.root = bst.delete(bst.root, val)
print(f"Inorder after deleting {val}:")
bst.inorder(bst.root)
print()






        
        
        




