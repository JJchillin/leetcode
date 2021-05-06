#https://leetcode.com/problems/remove-duplicates-from-sorted-list/
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