class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s = ord(target)
        for i in letters:
            if ord(i) > s:
                return i
                break
        return letters[0]