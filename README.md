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

**Example:**

```python
"""
Problem: Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy
Pattern: Two Pointers

Problem Statement:
A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward and
backward. Given a string s, return true if it is a palindrome, or false otherwise.

Approaches:
1. Filter & Reverse: O(n) time, O(n) space
2. Two Pointers: O(n) time, O(1) space

Tradeoffs:
- Approach 1: Most readable, but allocates a cleaned copy of the string
- Approach 2: Space-efficient; compares in-place without preprocessing

Key Insight:
In-place comparison with two pointers eliminates the need for string preprocessing,
achieving O(1) space complexity while maintaining O(n) time.
"""


# Approach 1: Filter & Reverse | Time: O(n) | Space: O(n)
# Strategy: Build a cleaned lowercase string and compare with its reverse
def is_palindrome_filter(s: str) -> bool:
    """Build a cleaned lowercase string and compare with its reverse."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


# Approach 2: Two Pointers | Time: O(n) | Space: O(1)
# Strategy: Compare from both ends, skipping non-alphanumeric characters
def is_palindrome_two_pointers(s: str) -> bool:
    """Compare characters from both ends, skipping non-alphanumeric."""
    left, right = 0, len(s) - 1
    while left < right:
        # Move left pointer to next alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1
        
        # Move right pointer to previous alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    test_cases = [
        # Basic palindromes
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        
        # Edge cases
        (" ", True),          # empty after filtering
        ("a", True),          # single character
        ("ab", False),        # two different characters

        # Numbers and special characters
        ("0P", False),
        ("a.b,c;c:b!a", True),
        ("A1b2B1a", True),

        # Case sensitivity
        ("Aa", True),
        ("Ab", False),
    ]

    for s, expected in test_cases:
        assert is_palindrome_filter(s) == expected, f"Filter failed for: '{s}'"
        assert is_palindrome_two_pointers(s) == expected, f"Two pointers failed for: '{s}'"

    print("All tests passed")
```

All functions use a descriptive suffix (`_brute`, `_sort`, `_filter`, `_counter`, `_early_exit`, `_two_pointers`, etc.). Boolean predicates use `is_*` or `has_*` as a prefix (e.g. `is_palindrome_filter`, `has_duplicate_early_exit`); other functions use the problem name as a prefix (e.g. `two_sum_brute`, `three_sum_two_pointers`).

Note: not all problems need multiple approaches - only when different solutions offer distinct insights or handle different constraints.

## Progress

- Problems solved: 4
- Patterns covered: 2/16

See [PATTERNS.md](PATTERNS.md) for all problems grouped by pattern.

## Resources

- https://leetcode.com
- https://neetcode.io

## License

MIT
