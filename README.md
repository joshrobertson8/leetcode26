# 🏆 LeetCode Solutions Repository

This repository contains **120+ LeetCode problems** organized according to **LeetCode's official categories** with **multiple solution approaches** showcasing optimization journeys and different algorithmic techniques.

## 📊 Repository Statistics

- **Total Problems**: 120
- **Total Solutions**: 254+ (multiple solutions per problem)
- **Problems with Multiple Solutions**: 59 (49.2% of all problems)
- **Categories**: 11 official LeetCode categories
- **Difficulties**: Easy (77), Medium (43)

## 🎯 Multiple Solutions Approach

### Why Multiple Solutions?

This repository preserves **the journey of optimization** - showing how solutions evolve from initial working code to optimized implementations. Each timestamped solution demonstrates:

- **Performance improvements** (runtime and memory optimization)
- **Different algorithmic approaches** (brute force → optimal)
- **Learning progression** over time
- **Various techniques** for the same problem

### Solution Distribution

| Solutions Count | Problems | Examples |
|----------------|----------|----------|
| **13 solutions** | 1 problem | Two Sum (showing evolution from O(n²) to O(n)) |
| **9 solutions** | 1 problem | Valid Parentheses (different stack implementations) |
| **7 solutions** | 1 problem | Remove Element (various two-pointer approaches) |
| **6 solutions** | 2 problems | Duplicate Zeros, Palindrome Number |
| **5 solutions** | 5 problems | Fruit Into Baskets, Rank Transform, etc. |
| **2-4 solutions** | 50 problems | Most problems showing 2-3 different approaches |

### 🚀 Top Optimization Examples

1. **Two Sum**: 2199ms → 0ms (100% improvement) + added hash map approach
2. **Valid Palindrome**: 982ms → 8ms (99.2% improvement) 
3. **Remove Duplicates**: 52ms → 0ms (100% improvement) + memory optimization
4. **Container With Most Water**: Multiple two-pointer implementations
5. **Majority Element**: Added both hash map and voting algorithm approaches

## 📁 Repository Structure

### Official LeetCode Categories

```
├── array/                    # 65 problems (most common)
│   ├── easy/                # Two Sum, Merge Sorted Array, etc.
│   └── medium/              # 3Sum, Product Except Self, etc.
├── string/                   # 27 problems  
│   ├── easy/                # Palindrome, Anagram, etc.
│   └── medium/              # Group Anagrams, Reverse Words, etc.
├── linked-list/             # 8 problems
│   ├── easy/                # Reverse, Merge, Cycle Detection
│   └── medium/              # Swap Nodes in Pairs
├── tree/                    # 5 problems
│   └── easy/                # Max Depth, Invert, Path Sum
├── dynamic-programming/     # 4 problems
│   ├── easy/                # Climbing Stairs, Best Time to Buy
│   └── medium/              # Best Time to Buy II
├── backtracking/           # 3 problems
│   └── medium/             # Permutations, Combinations
├── math/                   # 3 problems
│   └── easy/               # Happy Number, Power of Three
├── bit-manipulation/       # 2 problems
│   ├── easy/               # Single Number
│   └── medium/             # Reordered Power of 2
├── sliding-window/         # 1 problem
│   └── medium/             # Fruit Into Baskets
├── binary-search/          # 1 problem
│   └── easy/               # Binary Search
└── graph/                  # 1 problem
    └── medium/             # Number of Islands
```

### Problem Directory Structure

Each problem follows this structure:
```
category/difficulty/problem-name/
├── problem-name.txt                    # Plain English problem statement
├── YYYY-MM-DD HH.MM.SS - Solution1.py # Timestamped solutions
├── YYYY-MM-DD HH.MM.SS - Solution2.py # showing progression
└── YYYY-MM-DD HH.MM.SS - SolutionN.py # and optimization
```

## 🔍 How to Use This Repository

### 1. **Study by Category**
Focus on specific algorithmic patterns:
- **Arrays & Strings**: Most fundamental problems (92 total)
- **Dynamic Programming**: Classic DP patterns
- **Trees**: Essential tree traversal and manipulation
- **Linked Lists**: Pointer manipulation techniques

### 2. **Learn from Multiple Solutions**
For problems with multiple solutions:
- Start with the **earliest solution** (often brute force)
- Progress through **chronological improvements**
- Compare **runtime and memory optimizations**
- Understand **different algorithmic approaches**

### 3. **Interview Preparation**
- **Easy problems** (77): Master these first for coding interviews
- **Medium problems** (43): Practice for advanced positions
- **Multiple approaches**: Be ready to discuss trade-offs

## 🏅 Optimization Highlights

### Runtime Improvements
- **Two Sum**: O(n²) → O(n) with hash map
- **Valid Palindrome**: 982ms → 8ms (string preprocessing)
- **Binary Search**: Direct implementation improvements

### Memory Optimizations  
- **Fruit Into Baskets**: 17.1MB → 16.4MB (sliding window refinement)
- **Remove Duplicates**: Space-optimized in-place algorithms

### Algorithmic Evolution
- **Hash Map adoption**: Multiple problems show progression to hash-based solutions
- **Two Pointers**: Refinement of pointer manipulation techniques
- **Stack optimization**: Better stack implementations for parsing problems

## 📚 Learning Path Recommendation

### Beginner (Start Here)
1. **Array basics**: Two Sum, Remove Duplicates, Merge Sorted Array
2. **String fundamentals**: Palindrome, Anagram, Valid Parentheses  
3. **Linked List basics**: Reverse, Merge, Cycle Detection

### Intermediate
1. **Two Pointers**: Container With Most Water, 3Sum
2. **Dynamic Programming**: Climbing Stairs, Best Time to Buy Stock
3. **Tree Traversal**: Inorder, Max Depth, Invert Binary Tree

### Advanced  
1. **Backtracking**: Permutations, Combinations
2. **Graph algorithms**: Number of Islands
3. **Complex optimizations**: Study multiple solution approaches

## 🛠 Solution Evolution Analysis

This repository includes `analyze_solutions.py` which provides insights into:
- Problems with the most solution variations
- Performance improvement patterns
- Algorithmic technique adoption over time
- Learning progression tracking

Run analysis:
```bash
python analyze_solutions.py
```

## 🎯 Key Features

- ✅ **Official LeetCode categories** (matches LeetCode.com exactly)
- ✅ **Multiple solutions preserved** (49.2% of problems have 2+ solutions)
- ✅ **Plain text problem statements** (converted from HTML)
- ✅ **Chronological optimization tracking** (timestamped solutions)
- ✅ **Performance metrics** (runtime and memory in filenames)
- ✅ **Complete solution evolution** (from initial to optimized)

## 📈 Success Metrics

- **254+ total solutions** across 120 problems
- **Demonstrable optimization patterns** with quantified improvements
- **Comprehensive coverage** of fundamental algorithms and data structures
- **Multiple approaches** showing different ways to solve the same problem
- **Real learning progression** captured through timestamped iterations

---

*This repository showcases not just the final solutions, but the complete journey of learning and optimization - making it an invaluable resource for understanding how to approach, solve, and improve algorithmic solutions over time.*