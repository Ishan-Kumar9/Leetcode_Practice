class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        summ = sum(arr)
        num = summ // 3
        if summ % 3 != 0:
            return False

        count = 0
        n = 0
        for i in arr:
            n += i
            if n == num:
                n = 0
                count += 1
        
        return count >= 3
