class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        res = []
        sett = set(friends)
        for i in range(len(order)):
            if order[i] in sett:
                res.append(order[i])
        return res