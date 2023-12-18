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

    def height(self):
        return self.root.height()

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

print(tree.height())
