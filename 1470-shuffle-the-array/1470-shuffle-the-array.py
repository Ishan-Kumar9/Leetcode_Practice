class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        s = []
        j = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                s.append(nums[j])
                j += 1
            else:
                s.append(nums[n])
                n += 1
        return s