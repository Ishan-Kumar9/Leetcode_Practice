class Solution:
    def countPoints(self, rings: str) -> int:
        b = set()
        g = set()
        r = set()
        for i in range(0, len(rings)-1, 2):
            if rings[i] == "B":
                b.add(int(rings[i+1]))
            elif rings[i] == "R":
                r.add(int(rings[i+1]))
            else:
                g.add(int(rings[i+1]))

        cnt = 0
        for i in range(10):
            if i in b and i in g and i in r:
                cnt += 1
        return cnt