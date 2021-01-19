import random

class Node:
    def __init__(self,root):
        self.root = root
        self.rchild = None
        self.lchild = None

    def get_root(self):
        return self.root

    def get_right(self):
        return self.rchild()

    def get_left(self):
        return self.lchild

    def height(self):

        if self.child_free():
            return 0
        elif self.has_right_only():
            return self.rchild.height()+1
        elif self.has_left_only():
            return self.lchild.height()+1
        else:
            if self.rchild.height() > self.lchild.height():
                return self.rchild.height() + 1
            else:
                return self.lchild.height() + 1

    def balance_factor(self):
        if self.child_free():
            return 0
        elif self.has_right_only():
            return -1 - self.rchild.height()
        elif self.has_left_only():
            return self.lchild.height() - (-1)
        else:
            return self.lchild.height() - self.rchild.height()


    def add(self, value):
        if value >= self.root:
            if self.rchild:
                self.rchild.add(value)
            else:
                self.rchild = Node(value)
        else:
            if self.lchild:
                self.lchild.add(value)
            else:
                self.lchild = Node(value)

    def child_free(self):
        if not self.rchild and not self.lchild:
            return True
        else:
            return False

    def has_left_only(self):
        if self.lchild and not self.rchild:
            return True
        else:
            return False

    def has_right_only(self):
        if self.rchild and not self.lchild:
            return True
        else:
            return False

    def inorder(self):
        if self.root:
            if self.lchild and not self.rchild:
                self.lchild.inorder()
                print(self.root)
            elif not self.lchild and self.rchild:
                print(self.root)
                self.rchild.inorder()
            elif self.rchild and self.lchild:
                self.lchild.inorder()
                print(self.root)
                self.rchild.inorder()
            else:
                print(self.root)
        else:
            print('Empty')

    def __str__(self):
        if self.child_free():
            return f'[{self.lchild}-{self.root}-{self.lchild}]'
        elif self.has_left_only():
            return f'[{self.lchild.root}-{self.root}-{self.rchild}]'
        elif self.has_right_only():
            return f'[{self.lchild}-{self.root}-{self.rchild.root}]'
        else:
            return f'[{self.lchild.root}-{self.root}-{self.rchild.root}]'



class AVL:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head:
            self.head.add(value)
            if self.head.balance_factor() > 1:
                #left overweighted
                pass
        else:
            self.head = Node(value)

    def inorder(self):
        return self.head.inorder()

    def left_rotate(self, node):
        right = node.rchild
        temp = right.lchild
        node.rchild = temp
        right.lchild = node

        return right

    def right_rotate(self,node):
        left = node.lchild
        temp = left.rchild
        node.lchild = temp
        left.rchild = node

        return left



if __name__ == '__main__':
    n1 = Node(10)
    n1.add(11)
    n1.add(12)
    n1.add(13)

    print(n1.balance_factor())
    '''tree = AVL()
    for i in [random.randint(0,100) for l in range(10)]:
        print(i)
        tree.insert(i)
    print(tree.head.height())'''