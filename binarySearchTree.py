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

    def minRSubtree(self, curr):
        if curr.lchild == None:
            return curr
        else:
            return self.minRSubtree(curr.lchild)

    def deleteVal(self, key):
        self._deleteVal(self.root, None, None, key)

    def _deleteVal(self, curr, prev, isLeft, key):
        if curr:
            if key == curr.data:
                if curr.lchild and curr.rchild:
                    minChild = self.minRSubtree(curr.rchild)
                    curr.data = minChild.data
                    self._deleteVal(curr.rchild, curr, False, minChild.data)
                elif curr.lchild == None and curr.rchild == None:
                    if prev:
                        if isLeft:
                            prev.lchild = None
                        else:
                            prev.rchild = None
                    else:
                        self.root = None
                elif curr.lchild == None:
                    if prev:
                        if isLeft:
                            prev.lchild = curr.rchild
                        else:
                            prev.rchild = curr.rchild
                    else:
                        self.root = curr.rchild
                else:
                    if prev:
                        if isLeft:
                            prev.lchild = curr.lchild
                        else:
                            prev.rchild = curr.lchild
                    else:
                        self.root = curr.lchild
            elif key < curr.data:
                self._deleteVal(curr.lchild, curr, True, key)
            elif key > curr.data:
                self._deleteVal(curr.rchild, curr, False, key)
        else:
            print(f"{key} not found in tree")

# Tests
tree = BST()
tree.insert("F")
tree.insert("C")
print("Test deleting leaf node which is left child of parent")
tree.inOrder()
tree.deleteVal("C")
tree.inOrder()
tree.insert("G")
print("Test deleting leaf node which is right child of parent")
tree.inOrder()
tree.deleteVal("G")
tree.inOrder()
tree.insert("A")
print("Test deleting parent/root node which has one child")
tree.inOrder()
tree.deleteVal("F")
tree.inOrder()
print("Test deleting root node which has no children")
tree.inOrder()
tree.deleteVal("A")
tree.inOrder()
tree.insert("F")
tree.insert("C")
tree.insert("G")
tree.insert("A")
tree.insert("B")
tree.insert("K")
tree.insert("E")
tree.insert("H")
tree.insert("D")
tree.insert("I")
tree.insert("M")
tree.insert("J")
tree.insert("L")
tree.inOrder()
tree.deleteVal("F")
tree.inOrder()
tree.inOrder()
tree.deleteVal("K")
tree.inOrder()
tree.inOrder()
tree.deleteVal("C")
tree.inOrder()
tree.deleteVal("Z")
