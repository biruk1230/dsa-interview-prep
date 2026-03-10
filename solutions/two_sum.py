"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Pattern: Arrays & Hashing

Problem Statement:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Follow up: Return the answer with the smaller index first.

Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.

Approaches:
1. Brute Force: O(n^2) time, O(1) space
2. Sorting with Two Pointers: O(n log n) time, O(n) space (due to sorting)
3. Two-pass Hash Map: O(n) time, O(n) space
4. One-pass Hash Map: O(n) time, O(n) space

Tradeoffs:
- Approach 1: Simple and straightforward, but inefficient for large inputs
- Approach 2: Faster than brute force, but sorting changes indices and requires extra space to track original indices
- Approach 3: Linear time, but requires two passes through the array
- Approach 4: Linear time, single pass; returns immediately when complement is found since we check before inserting

Key Insight:
Using a hash map allows for O(1) average time complexity for lookups, enabling a single-pass solution that finds the complement of each number as we iterate through the array.
"""

# Approach 1: Brute Force | Time: O(n^2) | Space: O(1)
# Strategy: Check every pair of elements for a sum equal to target
def two_sum_brute(nums: list[int], target: int) -> list[int]:
    """Check every pair of elements for a sum equal to target."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# Approach 2: Sorting with Two Pointers | Time: O(n log n) | Space: O(n)
# Strategy: Sort a copy of the array while keeping track of original indices, then use two pointers to find the target sum
def two_sum_sort(nums: list[int], target: int) -> list[int]:
    """Preserve original indices, sort by value, then two-pointer."""
    pairs = [[num, i] for i, num in enumerate(nums)]
    pairs.sort()

    l, r = 0, len(pairs) - 1
    while l < r:
        curr = pairs[l][0] + pairs[r][0]
        if curr < target:
            l += 1
        elif curr > target:
            r -= 1
        else:
            return [min(pairs[l][1], pairs[r][1]),
                    max(pairs[l][1], pairs[r][1])]
    return []


# Approach 3: Two-pass Hash Map | Time: O(n) | Space: O(n)
# Strategy: Build a hash map of number to index in the first pass, then check for complements in the second pass
def two_sum_two_pass(nums: list[int], target: int) -> list[int]:
    """First pass builds the index map; second pass searches for complement."""
    num_to_index = {}
    for i, num in enumerate(nums):  # First pass: build the map
        num_to_index[num] = i
    for i, num in enumerate(nums):  # Second pass: check for complement
        complement = target - num
        if complement in num_to_index and num_to_index[complement] != i:  # Ensure we don't use the same element twice
            # i is always smaller: the loop encounters the earlier index first,
            # and num_to_index stores the last occurrence of each value
            return [i, num_to_index[complement]]
    return []


# Approach 4: One-pass Hash Map | Time: O(n) | Space: O(n)
# Strategy: Store each number's index; check if the complement has been seen before inserting
def two_sum_one_pass(nums: list[int], target: int) -> list[int]:
    """Store seen numbers and return indices when the complement is found."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]  # seen[complement] < i guaranteed - we only store indices before the current one
        seen[num] = i
    return []


if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),              # duplicate values
        ([-1, -2, -3, -4, -5], -8, [2, 4]),  # negative numbers
        ([0, 4, 3, 0], 0, [0, 3]),       # zero values
        ([-3, 4, 3, 90], 0, [0, 2]),      # mixed positive and negative
        ([1, 2], 3, [0, 1]),             # minimal case
    ]

    for nums, target, expected in test_cases:
        assert two_sum_brute(nums, target) == expected, f"Brute failed for {nums}, target={target}"
        assert two_sum_sort(nums, target) == expected, f"Sort failed for {nums}, target={target}"
        assert two_sum_two_pass(nums, target) == expected, f"Two-pass failed for {nums}, target={target}"
        assert two_sum_one_pass(nums, target) == expected, f"One-pass failed for {nums}, target={target}"

    print("All tests passed")
