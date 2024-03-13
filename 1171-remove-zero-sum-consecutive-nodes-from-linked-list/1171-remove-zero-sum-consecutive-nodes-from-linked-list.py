# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeZeroSumSublists(self, head):
        # initialize sum of input
        prefix_sum = 0
        # store prefix sums and nodes
        prefix_sum_map = {}
        # dummy of val 0 points to the head of list
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current:
            # update prefix sum
            prefix_sum += current.val
            # check if current prefix sum has second occurence
            if prefix_sum in prefix_sum_map:
                # remove nodes from linked list between the two occurrences of prefix_sum
                prev = prefix_sum_map[prefix_sum].next
                curr_sum = prefix_sum + prev.val
                # remove nodes until current sum = prefix sum
                while curr_sum != prefix_sum:
                    # remove current sum, move node and update current sum
                    del prefix_sum_map[curr_sum]
                    prev = prev.next
                    curr_sum += prev.val
                # update next pointer 
                prefix_sum_map[prefix_sum].next = current.next
            else:
                # store prefix sum and node if its first occurence
                prefix_sum_map[prefix_sum] = current
            current = current.next
        
        return dummy.next