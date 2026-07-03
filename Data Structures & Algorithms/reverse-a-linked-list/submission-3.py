# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev,orig=None,head
        while orig:
            i=orig.next
            orig.next=rev
            rev=orig
            orig=i
        return rev