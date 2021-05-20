#https://leetcode.com/problems/remove-linked-list-elements/
#Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return head
        while head.val == val:
            head = head.next
            if head == None:
                return head
        itr = head
        while itr.next != None:
            if itr.next.val == val:
                itr.next = itr.next.next
            else:    
                itr = itr.next
        return head
