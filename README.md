# DSA Interview Prep

Solutions to common interview problems with pattern-based indexing and reusable templates.

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Structure

```
├── solutions/          # Problem implementations
├── templates/          # Reusable pattern templates
└── PATTERNS.md         # Problems indexed by pattern
```

## Solution Format

Each solution includes:
- Problem statement and LeetCode link
- Approach explanation
- Time and space complexity
- Working implementation with test cases

Example:

```python
"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy

Approach: Hash map for O(1) complement lookup
Time: O(n) | Space: O(n)
"""

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

## Progress

- Problems covered: 0
- Patterns covered: 0/16

See [PATTERNS.md](PATTERNS.md) for all problems grouped by pattern.

## Resources

- https://leetcode.com
- https://neetcode.io

## License

MIT
