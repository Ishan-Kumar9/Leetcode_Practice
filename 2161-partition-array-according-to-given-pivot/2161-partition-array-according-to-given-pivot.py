class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res1 = []
        res2 = []
        count = 0
        for i in range(len(nums)):
            if nums[i] < pivot:
                res1.append(nums[i])
            elif nums[i] == pivot:
                count += 1
            else:
                res2.append(nums[i])
        res = res1 + [pivot]*count + res2
        return res