class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        summ = 0
        ans = minn = float("inf")
        best = [float("inf")] * len(arr) 
        left = 0
        for right in range(len(arr)):
            summ += arr[right]

            while summ > target:
                summ -= arr[left]
                left += 1

            if summ == target:
                x = right - left + 1
                if left > 0 and best[left-1] != float("inf"):
                    ans = min(ans, x+best[left-1])
                minn = min(minn, x)
                
            best[right] = minn
        if ans == float("inf"):
            return -1
        return ans