class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print("Found it")
            return True  # Return True when the target is found

        if self.left and target < self.data:
            return self.left.search(target)

        if self.right and target > self.data:
            return self.right.search(target)

        # Return False when the target is not found
        print("Value not found")
        return False

class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)

# Binary tree construction
node = Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(4)
node.left.right = Node(7)

node.right.left = Node(3)
node.right.right = Node(20)

print(node.right.data)
print(node.right.left.data)

# Naming a tree
myTree = Tree(node, "Billionaire Tree")

print(myTree.name)
print(myTree.root.left.data)
print(myTree.root.right.data)

# Searching data
found = myTree.search(20)
print(found)
