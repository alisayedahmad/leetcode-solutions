#Valid Parentheses
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                print(char, top_element)
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack
# Test
if __name__ == "__main__":
    solution = Solution()
    result = solution.isValid("()[]{}")
    print(result)