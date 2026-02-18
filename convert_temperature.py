class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        fahrenheit = celsius * 1.80 + 32.0        
        kelvin = celsius + 273.15
        return [kelvin, fahrenheit]
    
#Test cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.convertTemperature(36.50))
    print(solution.convertTemperature(122.11))   