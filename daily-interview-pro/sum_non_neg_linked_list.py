# You are given two linked-lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# Here is the function signature as a starting point (in Python):
# Definition for singly-linked list.

from time import time

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        # Fill this in.
        if not l1:
            return l2
        if not l2: 
            return l1
        node = None
        iter_node = None
        carry = 0
        while l1 is not None and l2 is not None:
            result = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            if node is None:
                node = ListNode(result)
                iter_node = node
            else:
                temp_node = ListNode(result)
                iter_node.next = temp_node
                iter_node = temp_node
            l1 = l1.next
            l2 = l2.next
        # since we do not know if a carry happened in the last step in the while loop, 
        # we must use it here as well
        while l1 is not None:
            result = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            temp_node = ListNode(result)
            iter_node.next = temp_node
            iter_node = temp_node
            l1 = l1.next
            # since carry is 0 from now on, we can optimise operations since we do not
            # need the modulo and divide operations
            if carry == 0 and l1 is not None:
                iter_node.next = l1
                l1 = None
        while l2 is not None:
            result = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            temp_node = ListNode(result)
            iter_node.next = temp_node
            iter_node = temp_node
            l2 = l2.next
            if carry == 0 and l2 is not None:
                iter_node.next = l2
                l2 = None

        return node

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
# 7 0 8
