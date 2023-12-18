class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root, name = ''):
        self.root = root
        self.name = name

node = Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(4)
node.left.right = Node(7)

node.right.left = Node(3)
node.right.right = Node(20)

print(node.right.data)
print(node.right.left.data)

myTree = Tree(node, "Billionaire Tree")

print(myTree.name)
print(myTree.root.left.data)
print(myTree.root.right.data)