class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            temp = i
            while temp > 0:
                ld = temp % 10
                if ld == 0:
                    break
                
                elif i % ld == 0:
                    temp //= 10
                else:
                    break
            if temp == 0:
                res.append(i)

        return res