class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = set()

        for num in nums:
            if num in a:
                a.remove(num)
            else:
                a.add(num)

        return a.pop()