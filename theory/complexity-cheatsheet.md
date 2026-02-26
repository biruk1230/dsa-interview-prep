# Complexity Reference

Quick reference for time and space complexity analysis.

## Data Structures

| Structure | Access | Search | Insert | Delete | Notes |
|-----------|--------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) | O(n) | Random access |
| Hash Table | O(1) by key | O(1) avg, O(n) worst | O(1) avg, O(n) worst | O(1) avg, O(n) worst | Worst case: hash collisions |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) | Unbalanced: O(n) worst |
| Heap | O(1) peek | O(n) | O(log n) | O(log n) | Peek min/max is O(1) |
| Stack | O(1) peek | O(n) | O(1) | O(1) | Only access top |
| Queue | O(1) peek | O(n) | O(1) | O(1) | Only access front |

## Sorting Algorithms

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Mergesort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Heapsort | O(n log n) | O(n log n) | O(n log n) | O(1) |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |

## Common Patterns

| Pattern | Time | Space | Notes |
|---------|------|-------|-------|
| Sliding Window | O(n) | O(1) or O(k) | Each element visited at most twice |
| Two Pointers | O(n) | O(1) | Often O(n log n) if sorting needed |
| Binary Search | O(log n) | O(1) | Requires sorted input AND random access (arrays, not linked lists) |
| BFS | O(V+E) | O(V) | V=vertices, E=edges |
| DFS | O(V+E) | O(h) | h=height of recursion tree |
| Dynamic Programming | O(n×m) | O(n×m) | Often optimizable to O(n) space |

## How to Analyze Complexity

**Time:**
1. Count loops - each nested loop typically multiplies complexity
2. For recursion, write recurrence relation or draw recursion tree
3. Identify what n represents (array length, tree nodes, graph vertices, etc.)

**Space:**
1. Count auxiliary data structures (hash maps, arrays, etc.)
2. Add recursion stack depth for recursive solutions
3. Don't count input/output in space complexity

**Amortized Analysis:**
Some operations have varying cost but average out over time.
- **Example:** Dynamic array (Python list) append
  - Most appends: O(1) 
  - Occasional resize when full: O(n) to copy all elements
  - Amortized over many operations: O(1)
- **When it matters:** Understanding why hash tables, dynamic arrays, and some tree operations are "O(1) amortized"

**Common Patterns:**
- One loop: O(n)
- Two nested loops: O(n²)
- Divide and conquer: O(n log n)
- Trying all combinations: O(2ⁿ) or O(n!)
- Hash map lookup/insert: O(1) average, O(n) worst case
