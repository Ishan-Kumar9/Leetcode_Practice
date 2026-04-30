class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        rank = 1
        answer = [0] * n
        for i in range(n):
            maxx = max(score)
            ind = score.index(maxx)
            answer[ind] = rank
            rank += 1
            score[ind] = -1
        for i in range(n):
            if answer[i] == 1:
                answer[i] = "Gold Medal"
            elif answer[i] == 2:
                answer[i] = "Silver Medal"
            elif answer[i] == 3:
                answer[i] = "Bronze Medal"
            else:
                answer[i] = str(answer[i])
                
        return answer