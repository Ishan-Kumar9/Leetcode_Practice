class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direc = 1
        curr = 1
        while time > 0:
            if curr == n:
                direc = -1
            if curr == 1:
                direc = 1

            curr += direc
            time -= 1
        return curr