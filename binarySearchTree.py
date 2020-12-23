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
        '''left, root, right'''
        self._inOrder(self.root)
        print('')

    def _inOrder(self, curr):
        if curr:
            self._inOrder(curr.lchild)
            print(curr.data, end=' ')
            self._inOrder(curr.rchild)

    def preOrder(self):
        '''root, left, right'''
        self._preOrder(self.root)
        print('')

    def _preOrder(self, curr):
        if curr:
            print(curr.data, end=' ')
            self._preOrder(curr.lchild)
            self._preOrder(curr.rchild)

    def postOrder(self):
        '''left, right, root'''
        self._postOrder(self.root)
        print('')

    def _postOrder(self, curr):
        if curr:
            self._postOrder(curr.lchild)
            self._postOrder(curr.rchild)
            print(curr.data, end=' ')

    def findVal(self, key):
        '''calls the private method _findVal'''
        return self._findVal(self.root, key)

    def _findVal(self, curr, key):
        '''returns True if key is found in tree, False otherwise'''
        if curr:
            if key == curr.data:
                return "Value found in tree"
            elif key < curr.data:
                return self._findVal(curr.lchild, key)
            else:
                return self._findVal(curr.rchild, key)
        return 'Value not found in tree'

    def deleteVal(self, key):
        self._deleteVal(self.root, None, None, key)

    def _deleteVal(self, curr, prev, isLeft, key):
        if curr:
            if key == curr.data:
                if isLeft:
                    prev.lchild = None
                else:
                    prev.rchild = None
            elif key < curr.data:
                self._deleteVal(curr.lchild, curr, True, key)
            elif key > curr.data:
                self._deleteVal(curr.rchild, curr, False, key)
        else:
            print(f"{key} not found in tree")

tree = BST()
tree.insert("F")
tree.insert("G")
tree.inOrder()
tree.deleteVal("G")
tree.inOrder()


# tree.insert("G")
# tree.insert("A")
# tree.insert("B")
# tree.insert("K")
# tree.insert("H")
# tree.insert("E")
# tree.insert("D")
# tree.insert("I")
# tree.insert("M")
# tree.insert("J")
# tree.insert("L")
# tree.inOrder()
# tree.preOrder()
# tree.postOrder()
# print(tree.findVal("E"))    # value found
# print(tree.findVal("J"))    # value found
# print(tree.findVal("Z"))    # value not found
