"""
Problem: Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
Pattern: Arrays & Hashing

Problem Statement:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An anagram contains the exact same characters as another string, in any order.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.

Approaches:
1. Sorting: O(n log n) time, O(n) space
2. Fixed Array (26 chars): O(n) time, O(1) space, ASCII only
3. Counter (Pythonic): O(n) time, O(k) space, no early exit
4. Two Hash Maps: O(n) time, O(k) space (where k = unique characters), no early exit
5. Single Hash Map: O(n) time, O(k) space, no early exit
6. Hash Map with early exit: O(n) time, O(k) space, exits on first char count mismatch

Tradeoffs:
- Approach 1: Simple and works for any alphabet, but O(n log n)
- Approach 2: Fastest for ASCII; breaks for Unicode inputs - optimal "low-level" solution for initial constraints
- Approach 3: Concise and leverages Python's standard library, but uses O(k) space for the Counter - most readable for Python
- Approach 4: More verbose than Counter, but no imports needed; still O(k) space for the maps
- Approach 5: Similar to Approach 4 but uses one dict instead of two; same O(k) space asymptotically
- Approach 6: Same complexity as Approach 5 but also exits early on the first char count mismatch, which can save time in practice

Follow up (Unicode inputs):
- For Unicode, Approach 2 is not suitable. Approaches 1, 3, 4, 5, 6 can handle Unicode as they rely on hash maps or sorting that can work with any character set.

Key Insight:
Two strings are anagrams iff their character frequency maps are identical.
A length check short-circuits the most common mismatch case in O(1).
"""

from collections import Counter


# Approach 1: Sorting | Time: O(n log n) | Space: O(n)
# Strategy: Sort both strings; anagrams always produce identical sorted sequences
def is_anagram_sort(s: str, t: str) -> bool:
    """Sort both strings and compare - anagrams yield identical sorted output."""
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


# Approach 2: Fixed Array | Time: O(n) | Space: O(1) - lowercase ASCII only
# Strategy: Use a 26-element array indexed by char offset from 'a'
def is_anagram_array(s: str, t: str) -> bool:
    """Count frequencies in a fixed 26-element array using char offsets from 'a'."""
    if len(s) != len(t):
        return False
    count = [0] * 26 # One slot for each letter 'a'-'z'
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    return all(c == 0 for c in count)


# Approach 3: Counter (Pythonic) | Time: O(n) | Space: O(k) where k = unique chars
# Strategy: Build frequency counters for both strings using Python's Counter and compare
def is_anagram_counter(s: str, t: str) -> bool:
    """Compare character frequency counters built by Python's Counter."""
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


# Approach 4: Two Hash Maps | Time: O(n) | Space: O(k) where k = unique chars
# Strategy: Count frequencies in two separate maps; compare them at the end
def is_anagram_two_maps(s: str, t: str) -> bool:
    """Count frequencies in two separate hash maps and compare them."""
    if len(s) != len(t):
        return False
    count_s, count_t = {}, {}
    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    return count_s == count_t


# Approach 5: Single Hash Map | Time: O(n) | Space: O(k) where k = unique chars
# Strategy: Increment counts for s, decrement for t in one pass; anagram if all values reach zero
def is_anagram_one_map(s: str, t: str) -> bool:
    """Increment counts for s, decrement for t; anagram if all values reach zero."""
    if len(s) != len(t):
        return False
    count = {}
    for cs, ct in zip(s, t):
        count[cs] = count.get(cs, 0) + 1
        count[ct] = count.get(ct, 0) - 1
    return all(v == 0 for v in count.values())


# Approach 6: Hash Map with early exit | Time: O(n) | Space: O(k) where k = unique chars
# Strategy: Build count from s; for each char in t, exit early if its count is already zero
def is_anagram_early_exit(s: str, t: str) -> bool:
    """Build count from s; exit early if any char in t is absent or exhausted."""
    if len(s) != len(t):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if count.get(char, 0) == 0:  # char not in s, or already used up
            return False
        count[char] -= 1
    return True


if __name__ == "__main__":
    test_cases = [
        ("anagram", "nagaram", True),     # classic anagram
        ("abc", "abc", True),             # identical strings
        ("listen", "silent", True),       # anagram, all positions shuffled
        ("rat", "car", False),            # same length, different chars
        ("a", "ab", False),               # different lengths
        ("a", "a", True),                 # single char
        ("aab", "bba", False),            # same chars, different counts
    ]

    for s, t, expected in test_cases:
        assert is_anagram_sort(s, t) == expected, f"Sort failed for ('{s}', '{t}')"
        assert is_anagram_array(s, t) == expected, f"Array failed for ('{s}', '{t}')"
        assert is_anagram_counter(s, t) == expected, f"Counter failed for ('{s}', '{t}')"
        assert is_anagram_two_maps(s, t) == expected, f"Two-maps failed for ('{s}', '{t}')"
        assert is_anagram_one_map(s, t) == expected, f"One-map failed for ('{s}', '{t}')"
        assert is_anagram_early_exit(s, t) == expected, f"Early-exit failed for ('{s}', '{t}')"
    print("All tests passed")
