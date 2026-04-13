class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minn = float("inf")
        for i in range(len(nums)):
            if nums[i] == target:
                dist = abs(i - start)
                if dist < minn:
                    minn = dist
        return minn