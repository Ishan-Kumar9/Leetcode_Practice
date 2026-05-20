class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c = []
        seen_A = set()
        seen_B = set()

        for i in range(len(A)):
            if A[i] not in seen_A:
                seen_A.add(A[i])

            if B[i] not in seen_B:
                seen_B.add(B[i])

            c.append(len(seen_A.intersection(seen_B)))
        return c