"""
Problem: Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/
Difficulty: Medium
Pattern: Arrays & Hashing

Problem Statement:
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Approaches:
1. Sort by Frequency: O(n log n) time, O(n) space
2. Built-in (Pythonic): O(n log k) time, O(n) space
3. Min-Heap: O(n log k) time, O(n) space
4. Bucket Sort: O(n) time, O(n) space
5. (Honorable Mention) QuickSelect: O(n) average time, O(n^2) worst case, O(n) space

Tradeoffs:
- Approach 1: Simple and readable; sorting is the bottleneck
- Approach 2: Leverages Python's built-in functionality for clarity and efficiency
- Approach 3: More efficient for large n and small k; maintains a heap of size k
- Approach 4: Optimal time complexity; uses extra space for buckets
- Approach 5: Average O(n) time; can degrade to O(n^2) if pivot selection is poor

Key Insight:
Frequencies are bounded by the array length, so using frequency as a bucket index
turns the selection problem into a linear scan from highest to lowest bucket.
"""

from collections import Counter
import heapq
import random


# Approach 1: Sort by Frequency | Time: O(n log n) | Space: O(n)
# Strategy: Count frequencies, sort unique elements by frequency descending, take first k
def top_k_frequent_sort(nums: list[int], k: int) -> list[int]:
    """Count frequencies, sort by frequency descending, return top k."""
    count = Counter(nums)
    sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)  # Sort by the frequency (item[1]) in descending order
    return [num for num, _ in sorted_items[:k]]  # Return the first k keys


# Approach 2: Built-in (Pythonic) | Time: O(n log k) | Space: O(n)
# Strategy: Counter.most_common(k) uses heapq.nlargest internally
def top_k_frequent_builtin(nums: list[int], k: int) -> list[int]:
    """Return top k frequent elements using Counter.most_common."""
    return [num for num, _ in Counter(nums).most_common(k)]


# Approach 3: Min-Heap | Time: O(n log k) | Space: O(n)
# Strategy: Count frequencies, push into a min-heap of size k, pop when heap exceeds k
def top_k_frequent_heap(nums: list[int], k: int) -> list[int]:
    """Maintain a min-heap of size k keyed by frequency."""
    count = Counter(nums)
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)  # Removes the element with the lowest frequency
    return [num for _, num in heap]


# Approach 4: Bucket Sort | Time: O(n) | Space: O(n)
# Strategy: Use frequency as bucket index; collect elements from highest bucket down
def top_k_frequent_bucket(nums: list[int], k: int) -> list[int]:
    """Place elements into frequency buckets, then collect top k from highest bucket down."""
    count = Counter(nums)

    # Bucket index = frequency, max possible frequency = len(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)

    result = []
    # Scan buckets from highest frequency to lowest
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result


# Approach 5: (Honorable Mention) QuickSelect | Time: O(n) average, O(n^2) worst | Space: O(n)
# Strategy: Use quickselect to find the k-th most frequent element, then collect all elements with higher frequency
def top_k_frequent_quickselect(nums: list[int], k: int) -> list[int]:
    """Finds top-k frequent elements using iterative Quickselect on frequency."""
    count = Counter(nums)
    unique = list(count.keys())
    n = len(unique)
    target = n - k  # The index that will separate the top-k from the rest

    def partition(left: int, right: int) -> int:
        pivot_idx = random.randint(left, right)
        pivot_freq = count[unique[pivot_idx]]

        # 1. Move pivot to end
        unique[pivot_idx], unique[right] = unique[right], unique[pivot_idx]

        # 2. Lomuto partition - elements less frequent than pivot go left
        store_idx = left
        for i in range(left, right):
            if count[unique[i]] < pivot_freq:
                unique[store_idx], unique[i] = unique[i], unique[store_idx]
                store_idx += 1

        # 3. Move pivot to its final position
        unique[store_idx], unique[right] = unique[right], unique[store_idx]
        return store_idx

    left, right = 0, n - 1
    while left < right:
        pivot_idx = partition(left, right)
        if pivot_idx < target:
            left = pivot_idx + 1
        elif pivot_idx > target:
            right = pivot_idx - 1
        else:
            break

    # At this point, unique[target:] contains the k most frequent elements
    return unique[target:]


if __name__ == "__main__":
    # Helper: compare results independent of order
    def same_elements(result: list[int], expected: list[int]) -> bool:
        return sorted(result) == sorted(expected)

    test_cases = [
        # Standard case
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        # Single element, k=1
        ([1], 1, [1]),
        # All same frequency, k equals unique count
        ([1, 2, 3], 3, [1, 2, 3]),
        # Negative numbers
        ([-1, -1, -2, -2, -3], 2, [-1, -2]),
        # k=1, clear winner
        ([4, 4, 4, 1, 2, 3], 1, [4]),
        # Tied frequencies with distinct top k
        ([1, 1, 2, 2, 3, 3, 4], 3, [1, 2, 3]),
        # Large frequency gap
        ([5, 5, 5, 5, 5, 1, 2, 3, 4], 1, [5]),
    ]

    for nums, k, expected in test_cases:
        result_sort = top_k_frequent_sort(nums, k)
        assert same_elements(result_sort, expected), f"Sort failed for {nums}, k={k}: got {result_sort}"
        result_heap = top_k_frequent_heap(nums, k)
        assert same_elements(result_heap, expected), f"Heap failed for {nums}, k={k}: got {result_heap}"
        result_builtin = top_k_frequent_builtin(nums, k)
        assert same_elements(result_builtin, expected), f"Built-in failed for {nums}, k={k}: got {result_builtin}"
        result_bucket = top_k_frequent_bucket(nums, k)
        assert same_elements(result_bucket, expected), f"Bucket failed for {nums}, k={k}: got {result_bucket}"
        result_qs = top_k_frequent_quickselect(nums, k)
        assert same_elements(result_qs, expected), f"QuickSelect failed for {nums}, k={k}: got {result_qs}"

    print("All tests passed")
