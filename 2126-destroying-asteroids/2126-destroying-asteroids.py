class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort(reverse=True)
        for i in range(len(asteroids)-1,-1,-1):
            if asteroids[i] <= mass:
                mass += asteroids[i]
            else:
                return False
        return True