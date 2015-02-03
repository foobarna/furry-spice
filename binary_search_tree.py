__author__ = 'blink'


class Node():
    """An object representing a node in a tree. It has value, storage, left and
    right leafs as properties. Value acts as a key in a dictionary and storage
    as value. Same values can be added multiple times."""
    def __init__(self, value, storage=None):
        self._value = value
        self._storage = storage
        self._leftNode = None
        self._rightNode = None

    def setStorage(self, storage):
        self._storage = None

    def getStorage(self):
        return self._storage

    def setLeftLeaf(self, node):
        self._leftNode = node

    def setRightLeaf(self, node):
        self._rightNode = node

    def getLeftLeaf(self):
        return self._leftNode

    def getRightLeaf(self):
        return self._rightNode

    def getValue(self):
        return self._value

    def compare(self, node):
        """A compare function, used to sort nodes. TRUE if caller node is
        greater, FALSE otherwise."""
        return self._value > node.getValue()


class BinarySeachTree():
    def __init__(self, root=None, storage=None):
        if root is Node or root is None:
            self._root = root
        else:
            node = Node(root, storage)
            self._root = node

    def insert(self, value, storage=None):
        """Inserts a value as a node in the tree"""
        node = Node(value, storage)
        if self._root:
            self._insert(node, self._root)
        else:
            self._root = node

    def _insert(self, node, currentNode):
        # if value of current node is bigger than the one to be added
        # add it to left leaf, otherwise add to right one
        if currentNode.compare(node):
            if currentNode.getLeftLeaf():
                self._insert(node, currentNode.getLeftLeaf())
            else:
                currentNode.setLeftLeaf(node)
        else:
            if currentNode.getRightLeaf():
                self._insert(node, currentNode.getRightLeaf())
            else:
                currentNode.setRightLeaf(node)

    def printNodes(self):
        """Prints the trees nodes in order"""
        self._printNodes(self._root)
        print

    def _printNodes(self, node):
        if node is None:
            return None

        self._printNodes(node.getLeftLeaf())
        print node.getValue(),
        self._printNodes(node.getRightLeaf())

    def printNodesAndStorage(self):
        """Prints the trees nodes in order, together with their storage"""
        self._printNodesAndStorage(self._root)
        print

    def _printNodesAndStorage(self, node):
        if node is None:
            return None

        self._printNodesAndStorage(node.getLeftLeaf())
        print node.getValue(), ' - ', node.getStorage()
        self._printNodesAndStorage(node.getRightLeaf())

    def rangeValues(self, a, b):
        """Returns a list of node's values in the interval (a, b)"""
        if a > b:
            a, b = b, a

        return self._rangeValues(self._root, a, b)

    def _rangeValues(self, node, a, b):
        node_values = []
        if node is None:
            return None

        if node.getValue() > a:
            left_values = self._rangeValues(node.getLeftLeaf(), a, b)
            if left_values is not None:
                node_values.extend(left_values)
        if a < node.getValue() < b:
            node_values.append(node.getValue())
        if node.getValue() < b:
            right_values = self._rangeValues(node.getRightLeaf(), a, b)
            if right_values is not None:
                node_values.extend(right_values)

        return node_values
