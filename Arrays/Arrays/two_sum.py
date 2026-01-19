"""
LeetCode: Two Sum
Link: https://leetcode.com/problems/two-sum/

Pattern: Array + Hashing
"""

# --------------------------------------------------
# 🟥 Brute Force Approach
# --------------------------------------------------
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class SolutionBruteForce(object):
    def twoSum(self, nums, target):
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


# --------------------------------------------------
# 🟩 Optimal Approach (Hash Map)
# --------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(n)

class SolutionOptimal(object):
    def twoSum(self, nums, target):
        d = {}
        n = len(nums)

        for i in range(n):
            diff = target - nums[i]
            if diff in d:
                return [d[diff], i]
            d[nums[i]] = i
