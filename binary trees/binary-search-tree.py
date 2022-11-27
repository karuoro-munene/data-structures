class Node:
    def __init__(self, value):
        self.value = value
        self.left = None  # the left child
        self.right = None  # the right child

    def add(self, another):  # another node
        if another.value < self.value:  # left
            if self.left is None:
                self.left = another
            else:
                self.left.add(another)
        else:  # another.value => self.value # right
            if self.right is None:
                self.right = another
            else:
                self.right.add(another)

    def inorder(self, node):
        """
        left, parent, right
        :param node:
        :return:
        """
        if node:
            self.inorder(node.left)  # call the inorder method recursively on the left subtree till leaf node
            print(node.value)  # once we reach the leaf, print node value
            self.inorder(node.right)  # call the inorder method recursively on the right subtree till leaf node

    def preorder(self, node):
        """
        root,left,right
        :param node: the node
        :return:
        """
        if node:
            print(node.value)  # print node value
            self.preorder(node.left)  # call the inorder method recursively on the left subtree till leaf node
            self.preorder(node.right)  # call the inorder method recursively on the right subtree till leaf node

    def postorder(self, node):
        """
        left,right,node
        :param node:
        :return:
        """
        if node:
            self.preorder(node.left)  # call the inorder method recursively on the left subtree till leaf node
            self.preorder(node.right)  # call the inorder method recursively on the right subtree till leaf node
            print(node.value)  # print node value
