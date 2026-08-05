class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a1 = 0
        a2 = 0
        s1 = set(nums1)
        s2 = set(nums2)
        for i in nums1:
            if i in s2:
                a1 += 1
        for j in nums2:
            if j in s1:
                a2 += 1
        return [a1,a2]