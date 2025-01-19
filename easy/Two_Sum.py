# Problem: Two Sum
# Difficulty: Easy
# URL: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        """
        Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
        """
        hash_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i
        return []

if __name__ == "__main__":
    # Example test case
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()  # Create an instance of the Solution class
    result = solution.twoSum(nums, target)  # Call the twoSum method
    print("Output: " + str(result))



