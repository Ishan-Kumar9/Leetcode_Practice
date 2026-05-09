class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxx = 0
        for i in range(len(accounts)):
            summ = sum(accounts[i])
            maxx = max(summ, maxx)
        return maxx