class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        write_index = 1
        
        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[read_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1
        
        return write_index
# Test
if __name__ == "__main__":  
    solution = Solution()
    nums = [1, 1, 2]
    new_length = solution.removeDuplicates(nums)
    print(new_length)  # Output should be: 2
    print(nums[:new_length])  # Output should be: [1, 2]