class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        maxx = -1
        for i in range(len(nums)-k+1):
            unique = set(nums[i:i+k])
            for j in unique:
                freq[j] += 1
        for num, cnt in freq.items():
            if cnt == 1 and num > maxx:
                maxx = num
                
        return maxx