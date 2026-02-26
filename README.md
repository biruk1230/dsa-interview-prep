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

```python
"""
Problem: 3Sum
Link: https://leetcode.com/problems/3sum/
Difficulty: Medium
Pattern: Two Pointers

Problem Statement:
Find all unique triplets in array that sum to zero.

Key Insight:
Sorting transforms this into a repeated Two Sum problem.
The two-pointer phase is O(n) per fixed element → O(n²) total.
"""

from typing import List


# --- Approach 1: Brute Force ---
# Time: O(n³) | Space: O(1)
def three_sum_brute(nums: List[int]) -> List[List[int]]:
    pass


# --- Approach 2: Two Pointers (optimal) ---
# Time: O(n²) | Space: O(1) excluding output
def three_sum(nums: List[int]) -> List[List[int]]:
    pass


if __name__ == "__main__":
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum_brute([-1, 0, 1, 2, -1, -4]) == expected
    assert three_sum([-1, 0, 1, 2, -1, -4]) == expected
    print("All tests passed")
```

The canonical/optimal function uses the problem's snake_case name (`three_sum`). Suboptimal approaches get a suffix (`_brute`, `_dp`, `_recursive`, etc.).

## Progress

- Problems covered: 0
- Patterns covered: 0/16

See [PATTERNS.md](PATTERNS.md) for all problems grouped by pattern.

## Resources

- https://leetcode.com
- https://neetcode.io

## License

MIT
