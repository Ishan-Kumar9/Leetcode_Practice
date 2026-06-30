class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for i in s:
            if i != "]":
                stk.append(i)
            else:
                y = ""
                while stk[-1] != "[":
                    y = stk.pop() + y
                stk.pop()

                num = ""
                while stk and stk[-1].isdigit():
                    num = stk.pop() + num
                x = int(num)

                res = x * y
                stk.append(res)

        ans = "".join(stk)
        return ans