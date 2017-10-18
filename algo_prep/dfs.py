class Node(object):
    def __init__(self, value, children=None):
        self.value = value
        if children is None:
            self.children = []
        else:
            self.children = children

def dfs(tree, value): # Check that value is in tree
    if tree.value == value:
        return True
    else:
        if tree.children != []:
            return True in map(lambda subtree: dfs(subtree, value), tree.children)
        else:
            return False

if __name__ == '__main__':
    test_tree = Node(5, [
                    Node(3, [
                        Node(15),
                        Node(12)]),
                    Node(7, [
                        Node(11, [
                            Node(1),
                            Node(22),
                            Node(13),
                            Node(8)]),
                        Node(14)])])
    assert dfs(test_tree, 5)
    assert dfs(test_tree, 15)
    assert dfs(test_tree, 12)
    assert dfs(test_tree, 14)
    assert dfs(test_tree, 22)
    assert not dfs(test_tree, 999)
    assert not dfs(test_tree, 0)
    assert not dfs(test_tree, 33)
