class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        ans = 0
        pick = 0
        for i in range(len(cost)):
            if pick == 2:
                pick = 0
            else:
                ans += cost[i]
                pick += 1
        return ans