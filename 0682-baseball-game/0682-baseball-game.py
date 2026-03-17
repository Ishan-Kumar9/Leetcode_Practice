class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk= []

        for i in operations:
            if i == 'C':
                stk.pop()
            elif i == 'D':
                stk.append(2 * stk[-1])
            elif i == '+':
                res = stk[-1] + stk[-2]
                stk.append(res)
            else:
                stk.append(int(i))

        sum = 0
        for i in stk:
            sum += int(i)
        return sum