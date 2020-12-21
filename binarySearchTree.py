class Node:
    def __init__(self, key):
        self.data = key
        self.lchild = None
        self.rchild = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key
        else:
            self._insert(self.root, key)

    def _insert(self, curr, key):
        if key.data > curr.data:
            if curr.rchild == None:
                curr.rchild = key
            else:
                self._insert(curr.rchild, key)
        elif key.data < curr.data:
            if curr.lchild == None:
                curr.lchild = key
            else:
                self._insert(curr.lchild, key)

    def inOrder(self):
        pass

    def _inOrder(self, curr):
        pass

    def pre_order(self):
        '''root, left, right'''
        pass

    def _pre_order(self, curr):
        pass

    def post_order(self):
        '''left, right, root'''
        pass

    def _post_order(self, curr):
        pass

    def find_val(self, key):
        pass

    def _find_val(self, curr, key):
        pass

    def delete_val(self, key):
        pass

    def _delete_val(self, curr, prev, is_left, key):
        pass
