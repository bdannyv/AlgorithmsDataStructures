class Node:
    def __init__(self, root):
        self.par = root
        self.lc = None
        self.rc = None

    def insert(self, data):
        if data == self.par:
            return False

        elif data < self.par:
            if self.lc:
                return self.lc.insert(data)
            else:
                self.lc = Node(data)
                return True

        else:
            if self.rc:
                return self.rc.insert(data)
            else:
                self.rc = Node(data)
                return True

    def find(self, val):
        if val == self.par:
            return True
        elif val < self.par and self.lc:
            self.lc.find(val)
        elif val > self.par and self.rc:
            self.rc.find(val)
        else:
            return False

    def preorder(self):
        if self.par:
            print(self.par)
            if self.lc:
                self.lc.preorder()
            if self.rc:
                self.rc.preorder()
        else:
            return False

    def inorder(self):
        if self.par:
            if self.lc:
                self.lc.inorder()

            print(self.par)

            if self.rc:
                self.rc.inorder()
        else:
            return False

    def postorder(self):
        if self.par:
            if self.lc:
                self.lc.inorder()

            if self.rc:
                self.rc.inorder()

            print(self.par)
        else:
            return False

    def __str__(self):
        return f'parent-{self.par}\nleft child-{self.lc} right child-{self.rc}'

    def child_free(self):
        if not self.lc and not self.rc:
            return True
        else:
            return False


class Tree:
    def __init__(self):
        self.root = None

    def remove(self, data):
        if not self.root:
            return False

        parent = None
        node = self.root

        while node.par != data and not node.child_free():

            parent = node

            if data > parent.par:
                node = parent.rc
            else:
                node = parent.lc
        if node.par != data:
            print(f'There is no {data} in the tree')
            return False
        elif not node.rc and not node.lc:
            print('Child-Free!')
            node.par = None
        elif node.lc and not node.rc:
            print('has only left child')
            node.par = node.lc.par
            node.lc.par = None
        elif node.rc and not node.lc:
            print('Real Parent')
            node.par = node.rc
        elif node.rc and node.lc:
            parent = node.par
            child = node.rc
            while child.lc:
                parent = child
                child = parent.lc # minimum value by the end of loop

            node.par = child.par
            child.par = None

    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = Node(value)
            return True

    def find(self, data):
        if self.root:
            self.root.find(data)
        else:
            return False

    def preorder(self):
        print('Preordered Tree')
        self.root.preorder()

    def postorder(self):
        print('Postordered Tree')
        self.root.postorder()

    def inorder(self):
        print('Inordered Tree')
        self.root.inorder()


if __name__ == '__main__':
    bst = Tree()
    bst.insert(4)
    bst.insert(1)
    bst.insert(3)
    bst.insert(2)
    bst.insert(25)
    bst.insert(26)
    bst.insert(24)
    bst.remove(4)
    bst.inorder()