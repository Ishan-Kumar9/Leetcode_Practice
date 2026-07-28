class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter
        freq = Counter(s)
        s_freq = dict(sorted(freq.items()))
        left  = []
        right = []
        mid = []

        for key in s_freq.keys():
            n = s_freq[key]
            if  n % 2 == 0:
                x = n//2
                left.append(key*x)
                right.append(key*x)
            else:
                x = n//2
                left.append(key*x)
                right.append(key*x)
                mid.append(key)
        right = right[::-1]
        ans = left + mid + right
        res = "".join(ans)
        return res