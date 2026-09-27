class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        for i in s:  
            if i == ')':
                temp = []
                while stk[-1] != '(':
                    temp.append(stk.pop())
                stk.pop()

                stk.extend(temp)

            else:
                stk.append(i)
        ans = ''.join(stk)
        return ans