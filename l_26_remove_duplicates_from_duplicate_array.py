from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        search = nums[0]
        while i < len(nums):
            if nums[i] == search:
                nums[i] = '_'
            else:
                search = nums[i]
            i += 1

        return len(nums) - nums.count('_')

sl = Solution()
print( sl.removeDuplicates([1,1,2]) )