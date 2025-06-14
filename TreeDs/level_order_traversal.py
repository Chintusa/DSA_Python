class Solution:
    def traverse(self, root, level, res):
        if not root:
            return
        if len(res) <= level:
            res.append([])  # create a new level list
        res[level].append(root.data)  # add node data to that level
        self.traverse(root.left, level + 1, res)  # left subtree
        self.traverse(root.right, level + 1, res)  # right subtree

    def levelOrder(self, root):
        res = []
        self.traverse(root, 0, res)
        return res
