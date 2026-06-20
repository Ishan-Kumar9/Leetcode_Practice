class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minn = float("inf")
        nums.sort()
        summ = 0

        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                x = nums[i] + nums[l] + nums[r]

                if x == target:
                    return target
                elif x > target:
                    r -= 1
                else:
                    l += 1
                diff = abs(x - target)
                if diff < minn:
                    summ = 0
                    minn = diff
                    summ += x

        return summ