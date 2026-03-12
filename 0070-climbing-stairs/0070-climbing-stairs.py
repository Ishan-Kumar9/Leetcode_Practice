class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        mapp = [0]*n
        mapp[0] = 1
        mapp[1] = 2

        for i in range(2,n):
            mapp[i] = mapp[i-2] + mapp[i-1]
        return mapp[n-1]