class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime = [True] * (n + 1)

        if n >= 0:
            prime[0] = False
        if n >= 1:
            prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if prime[i]:
                for j in range(i * i, n + 1, i):
                    prime[j] = False

        ans = []

        for i in range(2, n // 2 + 1):
            if prime[i] and prime[n - i]:
                ans.append([i, n - i])

        return ans