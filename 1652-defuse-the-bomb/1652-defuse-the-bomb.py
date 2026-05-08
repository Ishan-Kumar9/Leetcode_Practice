class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0]*n
        arr = code + code
        if k == 0:
            return res
        elif k > 0:
            for i in range(n):
                res[i] = sum(arr[i+1:i+k+1])
        else:
            k *= -1
            for i in range(n):
                res[i] = sum(arr[n+i-k:n+i])
        return res