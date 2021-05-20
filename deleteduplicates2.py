#https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
#Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        itr = head
        prev = itr
        lastprev = itr
        wasprevduplicate = False
        isduplicate = False
        while itr.next != None:
            if itr.val != itr.next.val and not isduplicate:
                prev = itr
                if prev.val == lastprev.val:
                    wasprevduplicate = False
            if itr.val != itr.next.val and isduplicate:
                if prev.val == itr.val:
                    prev = itr.next
                    head = prev
                else:
                    prev.next = itr.next
                isduplicate = False
                wasprevduplicate = True
            elif itr.val == itr.next.val:
                isduplicate = True
            lastprev = itr
            itr = itr.next
        
        if isduplicate:
            if prev.val == lastprev.val:
                head = None
            else:
                prev.next = None
        elif wasprevduplicate:
            pass
        elif prev.val == itr.val:
            head = itr.next
        elif lastprev.val == itr.val:
            prev.next = None
        return head
                
