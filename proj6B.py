# Define a Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        current = self.parent
        while current:
            level += 1
            current = current.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 4
        prefix = spaces + "|-- " if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


# Build the tree
def build_product_tree():
    root = Node("Electronics")

    laptop = Node("Laptop")
    laptop.add_child(Node("MacBook"))
    laptop.add_child(Node("Surface"))
    laptop.add_child(Node("ThinkPad"))

    cellphone = Node("Cell Phone")
    cellphone.add_child(Node("iPhone"))
    cellphone.add_child(Node("Google Pixel"))
    cellphone.add_child(Node("Vivo"))

    tv = Node("TV")
    tv.add_child(Node("Samsung"))
    tv.add_child(Node("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


# Call the function and print the tree
if __name__ == '__main__':
    root_node = build_product_tree()
    root_node.print_tree()
