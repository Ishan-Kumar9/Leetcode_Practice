class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            summ = 0
            while i > 0:
                last_digit = i % 10
                summ += last_digit
                i //= 10
            res.append(summ)
        return min(res)