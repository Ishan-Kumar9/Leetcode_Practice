class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)

        sorted_freq = dict(sorted(freq.items(), key=lambda item: item [1], reverse=True))
        
        res = []
        for num in sorted_freq:
            res.append(num)
            if len(res) == k:
                break
        return res