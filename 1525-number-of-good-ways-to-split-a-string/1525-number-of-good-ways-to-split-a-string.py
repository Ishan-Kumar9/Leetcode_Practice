class Solution:
    def numSplits(self, s: str) -> int:
        cnt = 0
        left = set()
        right_cnt = Counter(s)

        for i in s[:-1]:
            left.add(i)
            right_cnt[i] -= 1

            if right_cnt[i] == 0:
                del right_cnt[i]

            if len(left) == len(right_cnt):
                cnt += 1

        return cnt