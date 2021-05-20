#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            head = None
            return head
        length = 0
        lengthitr = head
        while lengthitr != None:
            lengthitr = lengthitr.next
            length = length + 1
        removeitr = head
        index = 0
        if index > length - n - 1:
            head = head.next
        else:
            while index < length - n - 1:
                removeitr = removeitr.next
                index = index + 1
            removeitr.next = removeitr.next.next
        return head
