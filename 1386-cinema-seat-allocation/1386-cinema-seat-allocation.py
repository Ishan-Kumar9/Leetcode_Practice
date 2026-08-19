class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        r = defaultdict(set)
        for row, col in reservedSeats:
            r[row].add(col)

        ans = 0
        for row, seat in r.items():
            left = all(c not in seat for c in range(2,6))
            middle = all(c not in seat for c in range(4,8))
            right = all(c not in seat for c in range(6,10))

            if left and right:
                ans += 2
            elif left or right or middle:
                ans += 1
        ans += 2 * (n-len(r))
        return ans