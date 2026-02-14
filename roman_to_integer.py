class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }    
        total = 0 
        for i in range(len(s)):
            if s[i] in romans:
                total += romans[s[i]]
                if i > 0 and romans[s[i]] > romans[s[i - 1]]:
                    total -= 2 * romans[s[i - 1]]
        return total    
    
# Test
if __name__ == "__main__":
    solution = Solution()
    result = solution.romanToInt("MCMXCIV")
    print(result)
    
