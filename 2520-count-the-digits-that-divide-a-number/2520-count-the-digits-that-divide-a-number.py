class Solution:
    def countDigits(self, num: int) -> int:
        cnt = 0
        s_num = str(num)
        for i in range(len(s_num)):
            if num % int(s_num[i]) == 0:
                cnt += 1
        return cnt
