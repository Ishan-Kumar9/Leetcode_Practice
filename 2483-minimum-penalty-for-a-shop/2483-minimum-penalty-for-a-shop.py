class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count('Y')
        best = penalty
        hour = 0

        for i in range(len(customers)):
            if customers[i] == 'Y':
                penalty -= 1
            else:
                penalty += 1

            if penalty < best:
                best = penalty
                hour = i + 1

        return hour