# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []

        curr = l1
        while curr:
            list1.append(str(curr.val))
            curr = curr.next

        curr = l2
        while curr:
            list2.append(str(curr.val))
            curr = curr.next
        
        list1 = list1[::-1]
        list2 = list2[::-1]

        l1_num = int("".join(list1))
        l2_num = int("".join(list2))

        summ = str(l1_num + l2_num)

        new = summ[::-1]

        dummy = ListNode()
        curr = dummy
        for i in new:
            curr.next = ListNode(int(i))
            curr = curr.next

        return dummy.next