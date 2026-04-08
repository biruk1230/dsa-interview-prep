"""
Problem: Encode and Decode Strings
Link: https://leetcode.com/problems/encode-and-decode-strings/
Difficulty: Medium
Pattern: Arrays & Hashing

Problem Statement:
Design an algorithm to encode a list of strings to a single string.
The encoded string is sent over the network and decoded back to the original list.

Follow up: Could you write a generalized algorithm to work on any possible set of characters?

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.

Approaches:
1. Escaped Delimiter: O(n) time, O(n) space
2. Length-Prefixed (chunked transfer): O(n) time, O(n) space

Tradeoffs:
- Approach 1: Natural to read in encoded form; decoding requires a character-by-character
  state machine to distinguish escaped delimiters from real ones.
- Approach 2: Slightly more overhead per string (length prefix) but decoding is simple index arithmetic.
- Both satisfy the follow-up. Approach 1 requires two reserved characters and escaping them; 
  Approach 2 needs no reserved characters at all.

Key Insight:
Using the string length as a self-describing prefix removes all ambiguity about where
each string ends. Boundaries are defined by length metadata rather than a reserved
character, so no escaping is needed regardless of what the strings contain - 
the encoding scheme is fully independent of the input character set.
"""


# Approach 1: Escaped Delimiter | Time: O(n) | Space: O(n)
# Strategy: Escape '\' as '\\' and '|' as '\|', then terminate each string with '|'
def encode_escaped(strs: list[str]) -> str:
    """Escape each string and terminate with '|'; empty list encodes to empty string."""
    result = []
    for s in strs:
        escaped = s.replace('\\', '\\\\').replace('|', '\\|')
        result.append(escaped + '|')
    return ''.join(result)


def decode_escaped(s: str) -> list[str]:
    """Scan for unescaped '|' terminators; '\\' consumes the next character literally."""
    result = []
    current = []
    i = 0
    while i < len(s):
        if s[i] == '\\':
            current.append(s[i + 1])  # next char is literal regardless of what it is
            i += 2
        elif s[i] == '|':
            result.append(''.join(current))
            current = []
            i += 1
        else:
            current.append(s[i])
            i += 1
    return result


# Approach 2: Length-Prefixed | Time: O(n) | Space: O(n)
# Strategy: Prefix each string with its character count and '#', then slice exactly that many chars when decoding
def encode_length_prefix(strs: list[str]) -> str:
    """Prefix each string with '<length>#'; no escaping needed."""
    return ''.join([f'{len(s)}#{s}' for s in strs])


def decode_length_prefix(s: str) -> list[str]:
    """Read length up to '#', then slice exactly that many characters."""
    result = []
    i = 0
    while i < len(s):
        j = s.index('#', i)  # find next '#' to determine length prefix
        length = int(s[i:j])
        result.append(s[j + 1:j + 1 + length])
        i = j + 1 + length
    return result


if __name__ == "__main__":
    test_cases = [
        # Basic cases
        (["lint", "code", "love", "you"], ["lint", "code", "love", "you"]),
        (["we", "say", ":", "yes"], ["we", "say", ":", "yes"]),

        # Edge cases - empty list and empty strings
        ([], []),
        ([""], [""]),
        (["", ""], ["", ""]),

        # Strings containing the delimiter character '|'
        (["a|b", "c|d"], ["a|b", "c|d"]),
        (["|", "||", "|||"], ["|", "||", "|||"]),

        # Strings containing the escape character '\'
        (["a\\b", "c\\\\d"], ["a\\b", "c\\\\d"]),

        # Strings containing '#' (length-prefix delimiter)
        (["3#abc", "10#hello"], ["3#abc", "10#hello"]),

        # Mixed special characters
        (["|\\#", "a|b\\c#d"], ["|\\#", "a|b\\c#d"]),

        # Single string
        (["hello"], ["hello"]),

        # Strings with all-ASCII special characters
        (["!@$%^&*()", "<>?/~`"], ["!@$%^&*()", "<>?/~`"]),
    ]

    for strs, expected in test_cases:
        result_escaped = decode_escaped(encode_escaped(strs))
        assert result_escaped == expected, (
            f"Escaped failed for {strs}: got {result_escaped}"
        )

        result_length = decode_length_prefix(encode_length_prefix(strs))
        assert result_length == expected, (
            f"Length-prefix failed for {strs}: got {result_length}"
        )

    print("All tests passed")
