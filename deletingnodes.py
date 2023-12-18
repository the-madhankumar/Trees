class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print("Found it")
            return True 

        if self.left and target < self.data:
            return self.left.search(target)

        if self.right and target > self.data:
            return self.right.search(target)
        
        print("Value not found")
        return False
    
    def traversePreorder(self):
        print(self.data)

        if self.left:
            self.left.traversePreorder()

        if self.right:
            self.right.traversePreorder()

    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()

        print(self.data)

        if self.right:
            self.right.traverseInorder()

    def traversePostorder(self):
        if self.left:
            self.left.traversePostorder()

        if self.right:
            self.right.traversePostorder()

        print(self.data)

    def getNodesAtDepth(self, depth, nodes=None):
        if nodes is None:
            nodes = []

        if depth == 0:
            nodes.append(self.data)
        else:
            if self.left:
                self.left.getNodesAtDepth(depth - 1, nodes)
            else:
                nodes.append(None)

            if self.right:
                self.right.getNodesAtDepth(depth - 1, nodes)
            else:
                nodes.append(None)

        return nodes
    
    def add(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.add(data)

        if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add(data)

    def findMin(self):
        if self.left:
            return self.left.findMin()
        return self.data
    
    def delete(self, target):
        if target < self.data:
            if self.left:
                self.left = self.left.delete(target)
        elif target > self.data:
            if self.right:
                self.right = self.right.delete(target)
        else:
            # Node with only one child or no child
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            # Node with two children
            min_val = self.right.findMin()
            self.data = min_val
            self.right = self.right.delete(min_val)
        
        return self

    # height
    def height(self):
        leftheight = self.left.height() + 1 if self.left else 0
        rightheight = self.right.height() + 1 if self.right else 0
        return max(leftheight, rightheight)

class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)
    
    def traversePreorder(self):
        self.root.traversePreorder()

    def traverseInorder(self):
        self.root.traverseInorder()

    def traversePostorder(self):
        self.root.traversePostorder()

    def getNodesAtDepth(self, depth):
        return self.root.getNodesAtDepth(depth)

    def height(self):
        return self.root.height()
    
    def add(self, data):
        self.root.add(data)

    def delete(self, target):
        self.root = self.root.delete(target)

# Example usage:
tree = Tree(Node(50), "Tree Traversal")
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.left.left = Node(10)
tree.root.left.right = Node(35)
tree.root.left.right.left = Node(30)
tree.root.left.right.right = Node(42)
tree.root.left.left.left = Node(5)
tree.root.left.left.right = Node(13)
tree.root.left.left.left.left = Node(2)

# Adding a new node with data 60
tree.add(60)

# Deleting node with data 35
tree.delete(35)

print(tree.getNodesAtDepth(2))
