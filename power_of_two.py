class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return (n & (n - 1)) == 0
#Test cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.isPowerOfTwo(1))  # True
    print(solution.isPowerOfTwo(16)) # True
    print(solution.isPowerOfTwo(3))  # False
    print(solution.isPowerOfTwo(4))  # True
    print(solution.isPowerOfTwo(5))  # False