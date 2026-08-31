# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head.next.next:
            return [-1,-1]
        cnt = 1
        res = []
        curr = head
        while curr and curr.next and curr.next.next:
            if curr.next.val > curr.val and curr.next.val > curr.next.next.val:
                res.append(cnt)
            elif curr.next.val < curr.val and curr.next.val < curr.next.next.val:
                res.append(cnt)
            curr = curr.next
            cnt += 1
        if len(res) < 2:
            return [-1,-1]
        maxx = res[-1] - res[0]
        minn = float("inf")
        
        for i in range(1,len(res)):
            ans = res[i] - res[i-1]
            minn = min(minn, ans)

        return [minn, maxx]