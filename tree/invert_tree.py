# Definition for singly-linked list.
class Tree(object):
    def __init__(self, val, l, r):
        self.val = val
        self.left = l
        self.right = r


def invert_tree(root):
    """
    :type node: Tree
    :rtype: void Do not return anything, modify node in-place instead.
    """
    if root is None:
        return
    else:
        root.left, root.right = root.right, root.left
        invert_tree(root.left)
        invert_tree(root.right)


def print_tree(root):
    if root is None:
        return
    print root.val
    print_tree(root.left)
    print_tree(root.right)


def main():
    head = Tree(4, Tree(2, Tree(1, None, None), Tree(3, None, None)),
                Tree(7, Tree(6, None, None), Tree(9, None, None)))
    invert_tree(head)
    print_tree(head)


if __name__ == '__main__':
    main()
