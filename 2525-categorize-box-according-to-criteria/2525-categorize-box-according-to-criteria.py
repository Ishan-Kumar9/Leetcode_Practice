class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        prod = 1
        s = []
        for i in [length, width, height]:
            prod *= i
            if i >= 10**4 or prod >= 10**9:
                s.append("Bulky")
                break
        if mass >= 100:
            s.append("Heavy")

        if len(s) == 2:
            return "Both"
        elif len(s) == 0:
            return "Neither"
        else:
            return s.pop()
