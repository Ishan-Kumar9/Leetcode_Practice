class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        Left_max = 0
        L = [0]*n
        for i in range(1,n):
            if height[i-1] > Left_max:
                Left_max = height[i-1]

            L[i] = Left_max

        Right_max = 0
        R = [0]*n
        for i in range(n-2,-1,-1):
            if height[i+1] > Right_max:
                Right_max = height[i+1]
            
            R[i] = Right_max
        
        total_water = 0
        for i in range(n):
            water = max(min(L[i], R[i]) - height[i], 0)

            total_water += water

        return total_water