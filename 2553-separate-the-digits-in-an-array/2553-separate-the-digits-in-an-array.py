class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            cont = []
            while i > 0:
                ld = i % 10
                cont.append(ld)
                i //= 10
            cont.reverse()
            ans.extend(cont)
        return ans