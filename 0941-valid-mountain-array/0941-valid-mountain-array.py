class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        maxx = arr.index(max(arr))

        if maxx == 0 or maxx == len(arr)-1:
            return False
        for i in range(maxx):
            if arr[i] >= arr[i+1]:
                return False
        for j in range(maxx,len(arr)-1):
            if arr[j] <= arr[j+1]:
                return False
        return True