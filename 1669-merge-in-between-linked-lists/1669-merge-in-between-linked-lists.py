# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        # find (a-1) node
        prev_a_node = list1
        for i in range (a-1):
            prev_a_node = prev_a_node.next
            
        # find bth node
        next_b_node = list1
        for i in range (b):
            next_b_node = next_b_node.next
        
        # connect prev_a_node to head of list2
        prev_a_node.next = list2
        
        # find last node of list2
        tail_list2 = list2
        while tail_list2.next:
            tail_list2 = tail_list2.next
        
        # connect tail to next_b_node
        tail_list2.next = next_b_node.next
        
        return list1
        
        
        