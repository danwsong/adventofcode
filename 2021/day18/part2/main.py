import functools

lines = open('input.txt').read().split('\n')

class TreeNode:
    def __init__(self, tree_input=None, parent=None):
        self.parent = parent
        if type(tree_input) is list:
            self.data = None
            self.prev = TreeNode(tree_input[0], self)
            self.next = TreeNode(tree_input[1], self)
        else:
            self.data = int(tree_input) if tree_input is not None else None
            self.prev = None
            self.next = None

    def get_rightmost_descendant(self):
        if self.data is not None:
            return self
        return self.next.get_rightmost_descendant()

    def get_predecessor(self):
        if self.prev is not None:
            return self.prev.get_rightmost_descendant()
        cur = self
        parent = cur.parent
        while parent is not None and parent.prev == cur:
            cur = parent
            parent = cur.parent
        return cur.parent
    
    def get_predecessor_leaf(self):
        cur = self
        successor = cur.get_predecessor()
        while successor is not None and successor.data is None:
            cur = successor
            successor = cur.get_predecessor()
        return successor
    
    def get_leftmost_descendant(self):
        if self.data is not None:
            return self
        return self.prev.get_leftmost_descendant()

    def get_successor(self):
        if self.next is not None:
            return self.next.get_leftmost_descendant()
        cur = self
        parent = cur.parent
        while parent is not None and parent.next == cur:
            cur = parent
            parent = cur.parent
        return cur.parent
    
    def get_successor_leaf(self):
        cur = self
        successor = cur.get_successor()
        while successor is not None and successor.data is None:
            cur = successor
            successor = cur.get_successor()
        return successor

    def try_explode(self, depth=0):
        if self.data is not None:
            return False
        if depth == 4:
            predecessor = self.prev.get_predecessor_leaf()
            if predecessor is not None:
                predecessor.data += self.prev.data
            successor = self.next.get_successor_leaf()
            if successor is not None:
                successor.data += self.next.data
            self.prev = None
            self.next = None
            self.data = 0
            return True
        return self.prev.try_explode(depth+1) or self.next.try_explode(depth+1)
    
    def try_split(self):
        if self.data is not None:
            if self.data >= 10:
                self.prev = TreeNode(self.data // 2, self)
                self.next = TreeNode(self.data - (self.data // 2), self)
                self.data = None
                return True
            else:
                return False
        return self.prev.try_split() or self.next.try_split()
    
    def __add__(self, other):
        new_snailfish = TreeNode()
        new_snailfish.prev = self
        self.parent = new_snailfish
        new_snailfish.next = other
        other.parent = new_snailfish
        while new_snailfish.try_explode() or new_snailfish.try_split():
            pass
        return new_snailfish
    
    def __str__(self):
        if self.data is not None:
            return str(self.data)
        return '[' + str(self.prev) + ', ' + str(self.next) + ']'
    
    def magnitude(self):
        if self.data is not None:
            return self.data
        return 3 * self.prev.magnitude() + 2 * self.next.magnitude()

max_magnitude = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        if i == j:
            continue
        a, b = TreeNode(eval(lines[i])), TreeNode(eval(lines[j]))
        max_magnitude = max(max_magnitude, (a + b).magnitude())
print(max_magnitude)
