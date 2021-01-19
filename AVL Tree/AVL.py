import random


class TreeNode:
    def __init__(self, root):
        self.parent = root
        self.lc = None
        self.rc = None
        self.height = 1

    def __str__(self):
        return f'[{self.lc}-{self.parent}-{self.rc}]'


class AVL:

    def find(self, root, val):
        if root.parent == val:
            return root

        result = None
        par = root
        if root.lc or root.rc:
            ch = root.rc if val > par.parent else root.lc
            if par.parent == val:
                result = par
            else:
                result = self.find(ch, val)

        return result

    def remove(self, root, val):
        print('_'*5,'deletion', '_'*5)
        print(f'root-{root} \nval-{val}\n')
        if not root:
            print('if not root:')
            return root

        elif val > root.parent:
            print(f'elif val > root.parent:')
            root.rc = self.remove(root.rc, val)
        elif val < root.parent:
            print(f'elif val < root.parent:')
            root.lc = self.remove(root.lc, val)
        else:
            print('else')
            if not root.lc:
                print(f'if not root.lc={root.lc}')
                return root.rc
            elif not root.rc:
                print(f'if not root.rc={root.rc}')
                return root.lc

            temp = self.min_node(root.rc)
            print(f'temp={temp}')
            root.parent = temp.parent
            print(f'after par subs root{root}')
            root.rc = self.remove(root.rc, temp.parent)
            print(f'after deletion without balancing. root = {root}')

        if root is None:
            print('If root is None')
            return root

        root.height = self.get_height(root)
        print(f'{root.height=}')
        balance = self.balance_f(root)
        print(f'root {balance=}')

        if balance > 1 and self.balance_f(root.lc) >= 0:
            print('right rotation')
            return self.right_rotation(root)

        if balance < -1 and self.balance_f(root.rc) <= 0:
            print('left rotation')
            return self.left_rotation(root)

        if balance > 1 and self.balance_f(root.lc) < 0:
            print('left-right rotation')
            root.lc = self.left_rotation(root.rc)
            return self.right_rotation(root)

        if balance < -1 and self.balance_f(root.rc) > 0:
            print('right-left rotation')
            root.rc = self.right_rotation(root.rc)
            return self.left_rotation(root)
        print('head is', root.parent)
        print('_'*5, 'The end of deletion', '_'*5)
        return root

    def min_node(self, root):
        if not root.lc:
            return root

        return self.min_node(root.lc)

    def insert(self, root, value):
        # standard insertion
        if not root:
            return TreeNode(value)
        elif value > root.parent:
            root.rc = self.insert(root.rc, value)
        else:
            root.lc = self.insert(root.lc, value)

        # height updating
        root.height = self.get_height(root)

        # balancing
        balance = self.balance_f(root)
        if balance > 1:
            if value <= root.lc.parent:
                return self.right_rotation(root)
            elif value > root.lc.parent:
                root.lc = self.left_rotation(root.lc)
                return self.right_rotation(root)
        elif balance < -1:
            if value > root.rc.parent:
                return self.left_rotation(root)
            elif value < root.rc.parent:
                root.rc = self.right_rotation(root.rc)
                return self.left_rotation(root)
        return root

    def right_rotation(self, root):
        left = root.lc
        tail = left.rc

        left.rc = root
        root.lc = tail

        root.height = self.get_height(root)
        left.height = self.get_height(left)
        return left

    def left_rotation(self, root):
        right = root.rc
        tail = right.lc

        # rotation
        right.lc = root
        root.rc = tail

        # height updating
        root.height = self.get_height(root)
        right.height = self.get_height(right)
        return right

    def get_height(self, root):
        if not root:
            return 0
        else:
            if not root.lc and not root.rc:
                return 1
            elif root.lc and not root.rc:
                return self.get_height(root.lc)+1
            elif not root.lc and root.rc:
                return self.get_height(root.rc) + 1
            else:
                if root.lc.height > root.rc.height:
                    return self.get_height(root.lc) + 1
                else:
                    return self.get_height(root.rc) + 1

    def balance_f(self, root):
        print(f'lc{root.lc} height is {self.get_height(root.lc)}')
        print(f'rc{root.rc} height is {self.get_height(root.rc)}')

        return self.get_height(root.lc) - self.get_height(root.rc)


if __name__ == '__main__':
    tree = AVL()
    node = TreeNode(10)
    for i in range(10):
        node = tree.insert(node, i)
    print(node)
    node = tree.remove(node, 1)