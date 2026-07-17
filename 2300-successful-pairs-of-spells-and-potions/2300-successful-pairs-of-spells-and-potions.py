class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pair = []
        potions.sort()
        
        for i in spells:
            minPotion = (success + i - 1) // i
            l, r = 0, len(potions)
            while l < r:
                mid = (l + r) // 2
                if potions[mid] < minPotion:
                    l = mid + 1
                else:
                    r = mid
            pair.append(len(potions) - l)
        return pair