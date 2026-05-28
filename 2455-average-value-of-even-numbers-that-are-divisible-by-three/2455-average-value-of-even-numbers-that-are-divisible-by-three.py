class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count = 0
        summ = 0
        for i in nums:
            if i % 6 == 0:
                summ += i
                count += 1
        if summ == 0:
            return summ
        return summ // count