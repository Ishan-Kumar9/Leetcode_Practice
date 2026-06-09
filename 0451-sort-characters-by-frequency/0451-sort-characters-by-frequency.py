class Solution:
    def frequencySort(self, s: str) -> str:
        set_s = set(s)
        dict_s = {}
        for i in set_s:
            dict_s[i] = s.count(i)

        sorted_dict = dict(sorted(dict_s.items(), key = lambda item: item[1], reverse = True))       

        ans = ""
        for key, value in sorted_dict.items():
            ans += (key*value)

        return ans