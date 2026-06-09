class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        i = 0
        while i < k:
            maxx = max(gifts)
            gifts.remove(maxx)
            gifts.append(int(maxx**0.5))
            i += 1
        return sum(gifts)