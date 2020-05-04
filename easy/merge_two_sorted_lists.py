# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if not l1 and not l2: 
            return None
        elif l1 and not l2:
            return l1
        elif l2 and not l1: 
            return l2

        # by setting it to an actual ListNode and using iter_node.next instead of just iter_node 
        # we can optimise the code by removing an if iter_node and an if begin_node check down the line 
        # that will be only be False once
        begin_node = ListNode(0)
        iter_node = begin_node

        while l1 and l2: 
            if l1.val <= l2.val:
                iter_node.next = l1
                l1 = l1.next
            else: 
                iter_node.next = l2
                l2 = l2.next
            iter_node = iter_node.next

        while l1: 
            iter_node.next = l1
            l1, iter_node = l1.next, iter_node.next    
        
        while l2: 
            iter_node.next = l2
            l2, iter_node = l2.next, iter_node.next

        return begin_node.next

if __name__ == "__main__":
    sol = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    
    _list = sol.mergeTwoLists(l1,l2)
    while _list:
        print(_list.val)
        _list = _list.next

# Runtime: 20 ms, faster than 93.53% of Python online submissions for Merge Two Sorted Lists.
# Memory Usage: 12.7 MB, less than 5.75% of Python online submissions for Merge Two Sorted Lists.