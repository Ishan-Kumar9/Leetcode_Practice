class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        n = len(nums)
        count = 0
        i = 0
        product = 1
        for j in range(n):
            product *= nums[j]

            while product >= k and i <= j:
                product //= nums[i]
                i += 1
        
            count += (j-i+1)
        
        return count