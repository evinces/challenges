"""2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Example

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def add_two_numbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        curr1 = l1
        curr2 = l2
        prod = ListNode(0)
        curr_prod = prod

        while curr1 or curr2:
            if curr1:
                curr_prod.val += curr1.val
                curr1 = curr1.next
            if curr2:
                curr_prod.val += curr2.val
                curr2 = curr2.next

            if curr_prod.val > 9:
                next_val = curr_prod.val // 10
                curr_prod.val = curr_prod.val % 10
            else:
                next_val = 0

            if curr1 or curr2 or next_val:
                curr_prod.next = ListNode(next_val)
                curr_prod = curr_prod.next

        return prod
