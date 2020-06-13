# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, head, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        this_node = head
        while this_node.next is not node:
            this_node = this_node.next
        this_node.next = node.next
        node.next = None


def main():
    # [4,5,1,9]
    head = ListNode(4)
    node5 = ListNode(5)
    node1 = ListNode(1)
    node9 = ListNode(9)
    head.next = node5
    node5.next = node1
    node1.next = node9
    solution = Solution().deleteNode(head, node5)
    this_node = head
    while this_node is not None:
        print this_node.val
        this_node = this_node.next


if __name__ == '__main__':
    main()