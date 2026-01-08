"""
Problem: Two sum
Leetcode link: https://leetcode.com/problems/two-sum/description/
Approach:
- Use a dictionary to store numbers and their indices.
- For each number, check if target - num exists.
- If yes, return indices.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[nums[i]] = i
