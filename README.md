# DSA Interview Prep

Solutions to common interview problems with pattern-based indexing and reusable templates.

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Structure

```
├── solutions/          # Problem implementations
├── templates/          # Reusable pattern templates
├── theory/             # Quick reference materials
└── PATTERNS.md         # Problems indexed by pattern
```

## Solution Format

Each solution includes:
- Problem statement and LeetCode link
- Approach explanation with complexity analysis
- Working implementation with test cases
- Multiple approaches when they offer distinct insights or handle different constraints

**Example with single approach:**

```python
"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Pattern: Arrays & Hashing

Problem Statement:
Given an array of integers and a target, return indices of two numbers that sum to target.

Key Insight:
Trading space for time - a hash map gives O(1) complement lookup vs O(n) array scan.
"""


# Hash Map | Time: O(n) | Space: O(n)
# Strategy: Store each number's index; check if the complement has been seen
def two_sum(nums: list[int], target: int) -> list[int]:
    """Store seen numbers and return indices when the complement is found."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
    ]

    for nums, target, expected in test_cases:
        assert two_sum(nums, target) == expected, f"Failed for {nums}, target={target}"

    print("All tests passed")
```

**Example with multiple approaches:**

```python
"""
Problem: Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy
Pattern: Two Pointers

Problem Statement:
Determine if a string is a palindrome, considering only alphanumeric
characters and ignoring case.

Approaches:
1. Filter & Reverse: O(n) time, O(n) space
2. (Optimal) Two Pointers: O(n) time, O(1) space

Tradeoffs:
- Approach 1: Most readable, but allocates a cleaned copy of the string
- Approach 2: Space-efficient; compares in-place without preprocessing

Key Insight:
Two pointers from both ends, skipping non-alphanumeric characters,
avoids allocating a cleaned copy of the string.
"""


# Approach 1: Filter & Reverse | Time: O(n) | Space: O(n)
# Strategy: Build a cleaned lowercase string and compare with its reverse
def is_palindrome_filter(s: str) -> bool:
    """Build a cleaned lowercase string and compare with its reverse."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


# Approach 2: Two Pointers (Optimal) | Time: O(n) | Space: O(1)
# Strategy: Compare from both ends, skipping non-alphanumeric characters
def is_palindrome(s: str) -> bool:
    """Compare characters from both ends, skipping non-alphanumeric."""
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ]

    for s, expected in test_cases:
        assert is_palindrome_filter(s) == expected, f"Filter failed for: '{s}'"
        assert is_palindrome(s) == expected, f"Optimal failed for: '{s}'"

    print("All tests passed")
```

The canonical/optimal function uses the problem's snake_case name (`is_palindrome`). Other approaches get a suffix (`_filter`, `_brute`, `_dp`, `_recursive`, etc.).

Note: not all problems need multiple approaches - only when different solutions offer distinct insights or handle different constraints.

## Progress

- Problems solved: 2
- Patterns covered: 2/16

See [PATTERNS.md](PATTERNS.md) for all problems grouped by pattern.

## Resources

- https://leetcode.com
- https://neetcode.io

## License

MIT
