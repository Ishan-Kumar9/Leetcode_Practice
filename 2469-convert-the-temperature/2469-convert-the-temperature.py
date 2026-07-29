class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        F = celsius * 1.8 + 32

        return [kelvin, F]