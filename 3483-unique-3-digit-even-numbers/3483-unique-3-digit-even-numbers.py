class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        freq = Counter(digits)
        cnt = 0
        for i in range(100,1000,2):
            temp = Counter(map(int, str(i)))
            if all(temp[d] <= freq[d] for d in temp):
                cnt += 1
        return cnt
