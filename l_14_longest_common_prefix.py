"""
14. Longest Common Prefix


Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.
"""

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # Sort the list of strings
        strs.sort()
        # Compare the first and last string in the sorted list
        first = strs[0]
        last = strs[-1]
        i = 0

        first_length = len(first)
        last_length = len(last)
        while i < first_length and i < last_length and first[i] == last[i]:
            i += 1
        return first[:i]


# Example usage
strs = ["flower"]
solution = Solution()
result = solution.longestCommonPrefix(strs)
print(result)