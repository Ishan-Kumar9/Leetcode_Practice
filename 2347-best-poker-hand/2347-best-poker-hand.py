class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        r = set(ranks)
        s = set(suits)
        if len(s) == 1:
            return "Flush"
        for i in r:
            if ranks.count(i) > 2:
                return "Three of a Kind"
        for i in r:
            if ranks.count(i) == 2:
                return "Pair"
        return "High Card"