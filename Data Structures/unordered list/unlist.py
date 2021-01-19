class Node:
    def __init__(self, val):
        self.root = val
        self.next = None

    def get_value(self):
        return self.root

    def get_next(self):
        if self.next:
            return self.next
        else:
            return None

    def set_next(self, data):
        if self.next:
            self.next.set_next(data)
        else:
            self.next = Node(data)

    def __str__(self):
        return f'[{self.root},{self.next}]'


class UnList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head:
            self.head.set_next(value)
        else:
            self.head = Node(value)

    def find(self, value):
        if self.head.get_value() == value:
            return True

        found = False
        par = self.head
        child = self.head.next

        while not found and par.get_next():
            if child.get_value() == value:
                found = True
                break
            par = child
            child = par.next

        return found

    def remove(self, value):
        print(f'We are looking for {value}')
        found = False
        par = None
        child = self.head

        while not found and child:
            if child.get_value() == value:
                found = True
                break
            par = child
            child = par.next


        print('parent = ', par)
        print('child = ', child)
        if found:
            if par:
                par.next = child.next
            else:
                self.head = child.next
        else:
            raise Exception(f'There is no {value} in the list')

    def __str__(self):
        return f'{self.head}'


if __name__ == '__main__':
    l = UnList()
    for i in range(10, 0, -1):
        l.append(i)
    for i in range(1, 11,2):
        l.remove(i)

    print(l)