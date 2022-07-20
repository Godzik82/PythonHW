from tree import Tree


def main():
    tree = Tree('Test')
    tree.create_node(1)
    tree.node.add_node('2')
    tree.node.add_node('3')
    tree.node.add_node(4)
    tree.node.children[0].add_node('23')
    tree.walk()

if __name__ == '__main__':
    main()