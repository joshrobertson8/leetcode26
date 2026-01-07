#!/usr/bin/env python3
"""
Complete the reorganization by creating missing category directories and ensuring all problems are properly placed.
"""

import os
import shutil
from pathlib import Path

def main():
    """Create missing category directories and move any remaining problems."""
    
    # Categories that should exist based on the reorganization output
    categories_needed = [
        'linked-list', 'tree', 'dynamic-programming', 'backtracking', 
        'graph', 'binary-search', 'sliding-window'
    ]
    
    # Create missing directories
    for category in categories_needed:
        for difficulty in ['easy', 'medium', 'hard']:
            os.makedirs(f"{category}/{difficulty}", exist_ok=True)
    
    # Create a simple mapping based on problem names/numbers we know should be in specific categories
    problem_mappings = {
        # Linked List problems
        'linked-list': [
            '21-merge-two-sorted-lists', '24-swap-nodes-in-pairs', '83-remove-duplicates-from-sorted-list',
            '141-linked-list-cycle', '160-intersection-of-two-linked-lists', '203-remove-linked-list-elements',
            '206-reverse-linked-list', '234-palindrome-linked-list', '908-middle-of-the-linked-list',
            '1411-convert-binary-number-in-a-linked-list-to-integer', '1618-delete-n-nodes-after-m-nodes-of-a-linked-list'
        ],
        
        # Tree problems
        'tree': [
            '94-binary-tree-inorder-traversal', '104-maximum-depth-of-binary-tree', '110-balanced-binary-tree',
            '112-path-sum', '226-invert-binary-tree', '617-merge-two-binary-trees'
        ],
        
        # Dynamic Programming
        'dynamic-programming': [
            '70-climbing-stairs', '121-best-time-to-buy-and-sell-stock', '122-best-time-to-buy-and-sell-stock-ii',
            '747-min-cost-climbing-stairs'
        ],
        
        # Backtracking
        'backtracking': [
            '46-permutations', '77-combinations', '2170-count-number-of-maximum-bitwise-or-subsets'
        ],
        
        # Graph
        'graph': [
            '200-number-of-islands'
        ],
        
        # Binary Search
        'binary-search': [
            '792-binary-search', '35-search-insert-position'
        ],
        
        # Sliding Window  
        'sliding-window': [
            '940-fruit-into-baskets'
        ]
    }
    
    # Check if any of these problems are in the wrong category
    moved_count = 0
    for category, problem_names in problem_mappings.items():
        for problem_name in problem_names:
            # Look for this problem in any directory
            found = False
            for current_dir in Path('.').iterdir():
                if not current_dir.is_dir() or current_dir.name.startswith('.'):
                    continue
                    
                for difficulty_dir in current_dir.iterdir():
                    if not difficulty_dir.is_dir():
                        continue
                        
                    for problem_dir in difficulty_dir.iterdir():
                        if problem_dir.is_dir() and problem_dir.name == problem_name:
                            found = True
                            current_category = current_dir.name
                            difficulty = difficulty_dir.name
                            
                            if current_category != category:
                                # Move to correct category
                                new_location = Path(f"{category}/{difficulty}/{problem_name}")
                                new_location.mkdir(parents=True, exist_ok=True)
                                
                                # Move all files
                                for file in problem_dir.iterdir():
                                    dest = new_location / file.name
                                    if not dest.exists():
                                        shutil.move(str(file), str(dest))
                                        
                                # Remove old empty directory
                                try:
                                    problem_dir.rmdir()
                                    print(f"✅ Moved {problem_name} from {current_category} to {category}")
                                    moved_count += 1
                                except:
                                    pass
                                    
                            break
                    if found:
                        break
                if found:
                    break
    
    print(f"\n🎉 Completed final organization!")
    print(f"Problems moved: {moved_count}")
    
    # Clean up any empty directories
    for item in Path('.').iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            try:
                for difficulty_dir in item.iterdir():
                    if difficulty_dir.is_dir():
                        try:
                            difficulty_dir.rmdir()  # Will only work if empty
                        except:
                            pass
                item.rmdir()  # Will only work if empty
            except:
                pass

if __name__ == "__main__":
    main()