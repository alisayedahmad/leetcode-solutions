"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
"""

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Test
if __name__ == "__main__":
    result = twoSum([2, 7, 11, 15], 9)
    print(result)  # [0, 1]