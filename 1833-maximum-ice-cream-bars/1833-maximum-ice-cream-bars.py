class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = len(costs)
        cnt = 0
        costs.sort()

        for i in costs:
            if i <= coins:
                cnt += 1
                coins -= i
        return cnt