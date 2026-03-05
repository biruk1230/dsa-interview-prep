"""
Problem: Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Pattern: Arrays & Hashing

Problem Statement:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

Approaches:
1. Brute-force: O(n^2) time, O(1) space
2. Sorting: O(n log n) time, O(n) space
3. Hash Set, length check: O(n) time, O(n) space, no early exit
4. Hash Set, early exit: O(n) time, O(n) space

Tradeoffs:
- Approach 1: Simple but too slow for large inputs
- Approach 2: Better than brute force, but still O(n log n) time
- Approach 3: Linear time, but always processes the full array
- Approach 4: Same complexity as 3, but exits as soon as duplicate is found

Key Insight:
Using a hash set allows for O(1) average time complexity for lookups,
making it the most efficient way to check for duplicates in a single pass through the array.
The early-exit variant is strictly better in practice - it short-circuits on the first duplicate found.
"""


# Approach 1: Brute-force | Time: O(n^2) | Space: O(1)
# Strategy: Check every pair of elements for a duplicate
def has_duplicate_brute(nums: list[int]) -> bool:
    """Check every pair of elements for a duplicate."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


# Approach 2: Sorting | Time: O(n log n) | Space: O(n)
# Strategy: Sort a copy and check adjacent elements for duplicates
# Note: nums.sort() sorts in-place and avoids allocating a new list, but
#       Python's Timsort still uses O(n) auxiliary space - same complexity
def has_duplicate_sort(nums: list[int]) -> bool:
    """Sort a copy and check adjacent elements for duplicates."""
    nums_sorted = sorted(nums)
    for i in range(1, len(nums_sorted)):
        if nums_sorted[i] == nums_sorted[i - 1]:
            return True
    return False


# Approach 3: Hash Set, length check (no early exit) | Time: O(n) | Space: O(n)
# Strategy: Convert to set and compare lengths - duplicates shrink the set
# Note: it always processes the full array
def has_duplicate_set_length(nums: list[int]) -> bool:
    """Compare list length to set length - duplicates reduce the set size."""
    return len(set(nums)) < len(nums)


# Approach 4: Hash Set, early exit | Time: O(n) | Space: O(n)
# Strategy: Track seen numbers; return True the moment a duplicate is found
def has_duplicate_early_exit(nums: list[int]) -> bool:
    """Track seen numbers and return True on the first duplicate found."""
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    test_cases = [
        ([1, 1, 2, 3, 4], True),                     # duplicate at start (best case for early exit)
        ([1, 2, 3, 1], True),                       # duplicate at end
        ([1, 2, 3, 4], False),                       # no duplicates
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),     # multiple duplicates
        ([0], False),                                 # single element
        ([-1, -1], True),                             # negative duplicates
        ([10**9, -10**9], False),                     # large numbers, no duplicate
        ([10**9, 10**9], True),                       # large numbers, duplicate
    ]

    for nums, expected in test_cases:
        assert has_duplicate_brute(nums) == expected, f"Brute failed for {nums}"
        assert has_duplicate_sort(nums) == expected, f"Sort failed for {nums}"
        assert has_duplicate_set_length(nums) == expected, f"Set failed for {nums}"
        assert has_duplicate_early_exit(nums) == expected, f"Early exit failed for {nums}"

    print("All tests passed")
