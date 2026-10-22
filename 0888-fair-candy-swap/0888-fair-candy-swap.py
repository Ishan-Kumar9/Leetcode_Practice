class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        sumA, sumB = sum(aliceSizes), sum(bobSizes)
        diff = (sumB - sumA) // 2
        bobSet = set(bobSizes)

        for a in aliceSizes:
            if a + diff in bobSet:
                return [a, a + diff]