class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        s = ""
        for i in binary:
            if i == "1":
                s += "0"
            else:
                s += "1"
        ans = int(s, 2)
        return ans