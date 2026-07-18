class Solution:
    def romanToInt(self, s: str) -> int:
        ref = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        ans = 0
        if len(s) == 1:
            return ref[s]
        i = 0
        while i < len(s):
            
            if i< len(s)-1 and ref[s[i]] < ref[s[i+1]]:
                ans += (ref[s[i+1]] - ref[s[i]])
                i += 2
                
            else:
                ans += ref[s[i]]
                i += 1
            
        return ans