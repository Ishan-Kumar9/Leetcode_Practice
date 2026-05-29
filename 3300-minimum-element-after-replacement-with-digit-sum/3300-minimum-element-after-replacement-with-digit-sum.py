class Solution:
    def minElement(self, nums: List[int]) -> int:
        minn = float("inf")
        for i in nums:
            summ = 0
            while i > 0:
                summ += i % 10
                i //= 10
            minn = min(minn, summ)
        return minn