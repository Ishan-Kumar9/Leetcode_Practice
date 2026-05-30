class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_e = 0
        sum_d = 0
        for i in nums:
            sum_e += i
            while i > 0:
                sum_d += i%10
                i //= 10
        return abs(sum_e - sum_d)