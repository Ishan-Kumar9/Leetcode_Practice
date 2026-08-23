class Solution:
    def sumGame(self, num: str) -> bool:
        mid = len(num) // 2
        left = right = 0
        lcount = rcount = 0
        for i in range(len(num)):
            if i < mid:
                if num[i].isdigit():
                    left += int(num[i])
                else:
                    lcount += 1
            else:
                if num[i].isdigit():
                    right += int(num[i])
                else:
                    rcount += 1

        if (lcount + rcount) % 2 != 0:
            return True
        
        return left - right != (rcount - lcount)*9//2