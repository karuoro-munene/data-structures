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
