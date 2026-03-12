"""
Problem: Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/
Difficulty: Medium
Pattern: Arrays & Hashing

Problem Statement:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An anagram contains the exact same characters as another string, in any order.

Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

Approaches:
1. Brute Force: O(n^2 * k) time, O(n * k) space - TLE on LeetCode
2. Sorted Key: O(n * k log k) time, O(n * k) space
3. Character Count Key: O(n * k) time, O(n * k) space
4. (Honorable Mention) Prime Product Key: O(n * k) time, O(n * k) space

Tradeoffs:
- Approach 1: Compares each string against every existing group; no canonical key, so O(n) lookups per string
- Approach 2: Simple and intuitive; sorting each string is the bottleneck
- Approach 3: Avoids sorting by using a frequency tuple as the key; faster for long strings
- Approach 4: Clever math trick (unique prime factorization), but overflows in fixed-width languages and big-int arithmetic erodes the O(n * k) advantage in Python

Key Insight:
Anagrams produce identical keys under any canonical form - whether sorted characters
or character frequency tuples. Grouping by canonical key collects all anagrams together
in O(1) per lookup, avoiding pairwise comparison.
"""

from collections import Counter, defaultdict


# Approach 1: Brute Force | Time: O(n^2 * k) | Space: O(n * k)
# Strategy: For each string, scan existing groups to find a matching anagram
# Note: TLE on LeetCode - included here to show why canonical keys matter
def group_anagrams_brute(strs: list[str]) -> list[list[str]]:
    """For each string, scan existing groups for an anagram match."""
    def is_anagram(s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return Counter(s) == Counter(t)

    groups = [] # list of lists
    for s in strs:
        found = False
        for group in groups:
            if is_anagram(s, group[0]):
                group.append(s)
                found = True
                break
        if not found:
            groups.append([s])
    return groups


# Approach 2: Sorted Key | Time: O(n * k log k) | Space: O(n * k)
# Strategy: Sort each string to form a canonical key; anagrams share the same sorted form
def group_anagrams_sort(strs: list[str]) -> list[list[str]]:
    """Group strings by their sorted character sequence as the key."""
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))  # Sorted characters form the key; lists aren't hashable, so we convert to a tuple
        groups[key].append(s)
    return list(groups.values())


# Approach 3: Character Count Key | Time: O(n * k) | Space: O(n * k)
# Strategy: Count character frequencies in a 26-element tuple; anagrams share the same counts
def group_anagrams_count(strs: list[str]) -> list[list[str]]:
    """Group strings by a 26-element character frequency tuple as the key."""
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26  # One for each letter 'a'-'z'
        for char in s:
            count[ord(char) - ord('a')] += 1
        groups[tuple(count)].append(s)  # lists aren't hashable, so we convert to a tuple
    return list(groups.values())


# Approach 4 (Honorable Mention): Prime Product Key | Time: O(n * k) | Space: O(n * k)
# Strategy: Assign each letter a unique prime; multiply primes for each string.
# By the Fundamental Theorem of Arithmetic, anagrams produce the same product.
# Caveats:
# - Math trick, not a reusable pattern
# - Overflows in fixed-width languages (Java/C++): the product of primes for a long string will quickly exceed the capacity of a 64-bit long.
#   For example, a string of 20 'z's would result in 101^20, which is massive
# - Python handles big ints, but arithmetic on huge numbers slows down,
#   eroding the theoretical O(n * k) advantage over sorted keys
def group_anagrams_prime(strs: list[str]) -> list[list[str]]:
    """Group strings by the product of per-character prime numbers."""
    # 26 prime numbers correspond to 'a' through 'z'
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
              53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    groups = defaultdict(list)
    for s in strs:
        product = 1
        for char in s:
            product *= primes[ord(char) - ord('a')]  # Multiply primes for each character
        groups[product].append(s)
    return list(groups.values())


if __name__ == "__main__":
    # Helper: compare grouped results independent of group order and inner order
    def same_groups(result: list[list[str]], expected: list[list[str]]) -> bool:
        normalize = lambda groups: sorted(sorted(g) for g in groups)
        return normalize(result) == normalize(expected)

    test_cases = [
        # Standard case
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        # Single empty string
        ([""], [[""]]),
        # Single non-empty string
        (["a"], [["a"]]),
        # All identical strings
        (["abc", "abc", "abc"], [["abc", "abc", "abc"]]),
        # No anagrams - each string is its own group
        (["abc", "def", "ghi"], [["abc"], ["def"], ["ghi"]]),
        # Multiple empty strings
        (["", ""], [["", ""]]),
        # Mixed lengths - no cross-length anagrams
        (["a", "ab", "ba"], [["a"], ["ab", "ba"]]),
    ]

    for strs, expected in test_cases:
        result_brute = group_anagrams_brute(strs)
        assert same_groups(result_brute, expected), f"Brute failed for {strs}"
        result_sort = group_anagrams_sort(strs)
        assert same_groups(result_sort, expected), f"Sort failed for {strs}"
        result_count = group_anagrams_count(strs)
        assert same_groups(result_count, expected), f"Count failed for {strs}"
        result_prime = group_anagrams_prime(strs)
        assert same_groups(result_prime, expected), f"Prime failed for {strs}"

    print("All tests passed")
