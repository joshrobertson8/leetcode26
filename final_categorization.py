#!/usr/bin/env python3
"""
Final categorization fix to ensure all problems are in correct LeetCode categories
"""

import os
import shutil
from pathlib import Path

def main():
    """Move problems to their correct official LeetCode categories."""
    
    # Comprehensive mapping based on LeetCode's official categories
    correct_categories = {
        # Dynamic Programming
        '70-climbing-stairs': ('dynamic-programming', 'easy'),
        '121-best-time-to-buy-and-sell-stock': ('dynamic-programming', 'easy'),  
        '122-best-time-to-buy-and-sell-stock-ii': ('dynamic-programming', 'medium'),
        '747-min-cost-climbing-stairs': ('dynamic-programming', 'easy'),
        
        # Backtracking  
        '46-permutations': ('backtracking', 'medium'),
        '77-combinations': ('backtracking', 'medium'),
        '2170-count-number-of-maximum-bitwise-or-subsets': ('backtracking', 'medium'),
        
        # Graph
        '200-number-of-islands': ('graph', 'medium'),
        
        # Sliding Window
        '940-fruit-into-baskets': ('sliding-window', 'medium'),
        '3790-fruits-into-baskets-ii': ('sliding-window', 'easy'),  # Related to sliding window
        
        # Two Pointers
        '15-3sum': ('two-pointers', 'medium'),
        '11-container-with-most-water': ('two-pointers', 'medium'),
        '167-two-sum-ii-input-array-is-sorted': ('two-pointers', 'medium'),
        '125-valid-palindrome': ('two-pointers', 'easy'),
        
        # Stack  
        '20-valid-parentheses': ('stack', 'easy'),
        '71-simplify-path': ('stack', 'medium'),
        
        # Heap
        '215-kth-largest-element-in-an-array': ('heap', 'medium'),
        '1014-k-closest-points-to-origin': ('heap', 'medium'),
        
        # Trie
        '208-implement-trie-prefix-tree': ('trie', 'medium'),
        
        # Hash Table
        '1-two-sum': ('hash-table', 'easy'),
        '49-group-anagrams': ('hash-table', 'medium'),
        '217-contains-duplicate': ('hash-table', 'easy'),
        '219-contains-duplicate-ii': ('hash-table', 'easy'),
        '169-majority-element': ('hash-table', 'easy'),
        '242-valid-anagram': ('hash-table', 'easy'),
        
        # Sorting
        '56-merge-intervals': ('sorting', 'medium'),
        '948-sort-an-array': ('sorting', 'medium'),
        '88-merge-sorted-array': ('sorting', 'easy'),
        '2210-find-target-indices-after-sorting-array': ('sorting', 'easy'),
        '1256-rank-transform-of-an-array': ('sorting', 'easy'),
        '941-sort-array-by-parity': ('sorting', 'easy'),
        
        # Greedy
        '55-jump-game': ('greedy', 'medium'),
        '134-gas-station': ('greedy', 'medium'),
        
        # Design
        '3678-design-task-manager': ('design', 'medium')
    }
    
    # Create all necessary directories
    all_categories = set()
    for category, difficulty in correct_categories.values():
        all_categories.add(category)
        os.makedirs(f"{category}/{difficulty}", exist_ok=True)
    
    print(f"Created directories for categories: {sorted(all_categories)}")
    
    # Move problems to correct categories
    moved_count = 0
    for problem_name, (correct_category, correct_difficulty) in correct_categories.items():
        # Look for this problem in current directories
        found = False
        for current_dir in Path('.').iterdir():
            if not current_dir.is_dir() or current_dir.name.startswith('.') or current_dir.name.endswith('.py'):
                continue
                
            for difficulty_dir in current_dir.iterdir():
                if not difficulty_dir.is_dir():
                    continue
                    
                for problem_dir in difficulty_dir.iterdir():
                    if problem_dir.is_dir() and problem_dir.name == problem_name:
                        found = True
                        current_category = current_dir.name
                        current_difficulty = difficulty_dir.name
                        
                        if current_category != correct_category or current_difficulty != correct_difficulty:
                            # Move to correct location
                            new_location = Path(f"{correct_category}/{correct_difficulty}/{problem_name}")
                            new_location.mkdir(parents=True, exist_ok=True)
                            
                            # Move all files
                            files_moved = 0
                            for file in problem_dir.iterdir():
                                dest = new_location / file.name
                                if not dest.exists():
                                    shutil.move(str(file), str(dest))
                                    files_moved += 1
                            
                            # Remove old directory
                            try:
                                problem_dir.rmdir()
                                print(f"✅ Moved {problem_name}: {current_category}/{current_difficulty} → {correct_category}/{correct_difficulty} ({files_moved} files)")
                                moved_count += 1
                            except Exception as e:
                                print(f"⚠️  Could not remove {problem_dir}: {e}")
                                
                        break
                if found:
                    break
            if found:
                break
    
    print(f"\n🎉 Final categorization complete!")
    print(f"Problems moved to correct categories: {moved_count}")
    
    # Count problems by category
    print(f"\n📊 FINAL CATEGORY DISTRIBUTION:")
    category_counts = {}
    total_solutions = 0
    
    for category_dir in Path('.').iterdir():
        if not category_dir.is_dir() or category_dir.name.startswith('.') or category_dir.name.endswith('.py'):
            continue
            
        problems_in_category = 0
        solutions_in_category = 0
        
        for difficulty_dir in category_dir.iterdir():
            if not difficulty_dir.is_dir():
                continue
                
            for problem_dir in difficulty_dir.iterdir():
                if problem_dir.is_dir():
                    problems_in_category += 1
                    # Count solution files
                    solutions_in_category += len([f for f in problem_dir.iterdir() if f.name.endswith('.py')])
        
        if problems_in_category > 0:
            category_counts[category_dir.name] = problems_in_category
            total_solutions += solutions_in_category
            print(f"  {category_dir.name}: {problems_in_category} problems, {solutions_in_category} solutions")
    
    print(f"\nTotal problems: {sum(category_counts.values())}")
    print(f"Total solutions: {total_solutions}")

if __name__ == "__main__":
    main()