class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        minn = float("inf")
        for i in range(len(landStartTime)):
            l_finish = landStartTime[i] + landDuration[i]
            for j in range(len(waterStartTime)):
                w_finish = max(l_finish, waterStartTime[j]) + waterDuration[j]
                minn = min(minn, w_finish)

        for i in range(len(waterStartTime)):
            w_finish = waterStartTime[i] + waterDuration[i]
            for j in range(len(landStartTime)):
                l_finish = max(w_finish, landStartTime[j]) + landDuration[j]
                minn = min(minn, l_finish)

        return minn