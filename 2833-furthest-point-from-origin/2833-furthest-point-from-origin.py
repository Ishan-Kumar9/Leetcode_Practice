class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        dist = 0
        c1 = moves.count("L")
        c2 = moves.count("R")
        if c1 < c2:
            x = 1
        else:
            x = -1
        for i in moves:
            if i == "L":
                dist -= 1
            elif i == "R":
                dist += 1
            else:
                dist += x
        return abs(dist)