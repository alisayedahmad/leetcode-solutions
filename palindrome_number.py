class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
# Test
if __name__ == "__main__":    
    solution = Solution()
    result = solution.isPalindrome(121)
    print(result)  # True