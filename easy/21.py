# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        if list1.val < list2.val:
            resListHead = list1
            list1 = list1.next
        else:
            resListHead = list2
            list2 = list2.next
            
        resList = resListHead
                
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                resList.next = list1
                list1 = list1.next
            else:
                resList.next = list2
                list2 = list2.next
            resList = resList.next
            
        if list1 != None:
            resList.next = list1
            
        if list2 != None:
            resList.next = list2
            
        return resListHead
        