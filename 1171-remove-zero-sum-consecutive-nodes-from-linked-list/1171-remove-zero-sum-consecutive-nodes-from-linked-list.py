# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeZeroSumSublists(self, head):
        prefix_sum = 0
        # Keep track of prefix sumss and nodes
        prefix_sum_map = {}
        # dummy 0 points to the head of list
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current:
            prefix_sum += current.val
            if prefix_sum in prefix_sum_map:
                # Remove nodes from the linked list between the two occurrences of prefix_sum
                prev = prefix_sum_map[prefix_sum].next
                curr_sum = prefix_sum + prev.val
                while curr_sum != prefix_sum:
                    del prefix_sum_map[curr_sum]
                    prev = prev.next
                    curr_sum += prev.val
                prefix_sum_map[prefix_sum].next = current.next
            else:
                prefix_sum_map[prefix_sum] = current
            current = current.next
        
        return dummy.next