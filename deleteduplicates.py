#https://leetcode.com/problems/remove-duplicates-from-sorted-list/
#Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        itr = head
        while itr.next != None:
            if itr.val == itr.next.val:
                itr.next = itr.next.next
            else:
                itr = itr.next
        return head
