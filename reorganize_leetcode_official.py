#!/usr/bin/env python3
"""
LeetCode Repository Reorganizer - Official Categories

This script reorganizes the repository to match LeetCode's official categories exactly.
It also ensures multiple solutions for the same problem are properly organized.
"""

import os
import re
import shutil
from pathlib import Path
from html import unescape
import html2text


def html_to_text(html_content):
    """Convert HTML content to plain text."""
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True
    h.ignore_emphasis = False
    h.body_width = 0
    
    text = h.handle(html_content)
    
    # Clean up the text
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # Remove bold markdown
    text = re.sub(r'\*(.*?)\*', r'\1', text)      # Remove italic markdown
    text = re.sub(r'`(.*?)`', r'\1', text)        # Remove code markdown
    text = re.sub(r'\n\s*\n\s*\n', '\n\n', text) # Remove excessive newlines
    text = text.strip()
    
    return text


def extract_difficulty_and_title(html_content):
    """Extract difficulty and clean title from HTML content."""
    # Extract difficulty
    difficulty_match = re.search(r'Difficulty:\s*(\w+)', html_content)
    difficulty = difficulty_match.group(1) if difficulty_match else 'Medium'
    
    # Extract title
    title_match = re.search(r'<h1>(\d+)\s*-\s*(.*?)</h1>', html_content)
    if title_match:
        number = title_match.group(1)
        title = title_match.group(2).strip()
        return difficulty.lower(), number, title
    
    return 'medium', '0', 'Unknown Problem'


def map_old_to_new_category(old_category, title, number):
    """Map old category structure to new LeetCode official categories."""
    title_lower = title.lower()
    
    # Direct mapping from old categories to new ones
    category_mapping = {
        'array-string': ['array', 'string'],  # Split into separate categories
        'linked-list': 'linked-list',
        'tree': 'tree', 
        'dynamic-programming': 'dynamic-programming',
        'graph': 'graph',
        'binary-search': 'binary-search',
        'heap': 'heap',
        'trie': 'trie',
        'backtracking': 'backtracking',
        'math-bit': ['math', 'bit-manipulation'],  # Split into separate categories
        'sliding-window': 'sliding-window',
        'two-pointers': 'two-pointers'
    }
    
    # Handle split categories
    if old_category == 'array-string':
        # Determine if it's more array or string focused
        array_keywords = ['array', 'sum', 'subarray', 'merge', 'rotate', 'remove element',
                         'remove duplicates', 'plus one', 'majority element', 'search insert',
                         'container', 'intervals', 'jump', 'sort', 'maximum', 'minimum']
        
        string_keywords = ['string', 'palindrome', 'anagram', 'substring', 'prefix', 'suffix',
                          'roman', 'word', 'length', 'reverse', 'pattern', 'ransom', 'subsequence']
        
        array_score = sum(1 for keyword in array_keywords if keyword in title_lower)
        string_score = sum(1 for keyword in string_keywords if keyword in title_lower)
        
        if string_score > array_score:
            return 'string'
        else:
            return 'array'
    
    elif old_category == 'math-bit':
        # Determine if it's math or bit manipulation
        bit_keywords = ['bit', 'single number', 'bits', 'bitwise', 'power of two', 'reordered power']
        
        if any(keyword in title_lower for keyword in bit_keywords):
            return 'bit-manipulation' 
        else:
            return 'math'
    
    # Direct mapping for other categories
    mapped = category_mapping.get(old_category, old_category)
    if isinstance(mapped, list):
        return mapped[0]  # Default to first option
    return mapped
    """Categorize problems using LeetCode's official categories."""
    title_lower = title.lower()
    number_int = int(number) if number.isdigit() else 0
    
    # LeetCode's official categories with their exact naming
    categories = {
        # Core data structures (most common)
        'array': [
            'array', 'two sum', 'subarray', 'merge', 'rotate', 'remove element',
            'remove duplicates', 'plus one', 'majority element', 'search insert',
            'container with most water', 'merge intervals', 'jump game', 'h-index',
            'gas station', 'product of array', 'kth largest element', 'sort',
            'maximum difference', 'rank transform', 'find target indices'
        ],
        
        'string': [
            'string', 'palindrome', 'anagram', 'substring', 'prefix', 'suffix', 'roman',
            'longest common', 'zigzag conversion', 'word pattern', 'isomorphic',
            'ransom note', 'is subsequence', 'length of last word', 'reverse words',
            'group anagrams', 'valid anagram', 'backspace string compare',
            'delete characters', 'shuffle string', 'count prefix and suffix'
        ],
        
        'hash-table': [
            'hash', 'contains duplicate', 'group anagrams', 'two sum', 'isomorphic strings',
            'word pattern', 'find lucky integer', 'majority element'
        ],
        
        'linked-list': [
            'linked list', 'merge two sorted lists', 'reverse linked list', 'middle of',
            'cycle', 'intersection', 'palindrome linked list', 'swap nodes', 'remove nth',
            'add two numbers', 'delete', 'convert binary number'
        ],
        
        'tree': [
            'tree', 'binary tree', 'depth', 'height', 'invert', 'symmetric', 'path sum',
            'balanced', 'diameter', 'lowest common ancestor', 'serialize', 'deserialize',
            'level order', 'preorder', 'inorder', 'postorder', 'traversal', 'merge two binary trees'
        ],
        
        'stack': [
            'valid parentheses', 'simplify path', 'min stack', 'evaluate expression',
            'daily temperatures', 'next greater element'
        ],
        
        'math': [
            'power of', 'factorial', 'prime', 'gcd', 'lcm', 'happy number', 'ugly number',
            'perfect square', 'integer to roman', 'palindrome number', 'reverse integer',
            'climbing stairs', 'fibonacci'
        ],
        
        'dynamic-programming': [
            'climbing stairs', 'house robber', 'coin change', 'longest increasing',
            'edit distance', 'unique paths', 'minimum path sum', 'decode ways', 'word break',
            'longest palindromic substring', 'palindrome partitioning', 'best time to buy',
            'maximum subarray', 'range sum query', 'paint house', 'delete and earn',
            'min cost climbing stairs', 'partition equal subset sum'
        ],
        
        'two-pointers': [
            'two pointers', 'two sum ii', 'three sum', 'four sum', 'trapping rain water',
            'container with most water', 'move zeroes', 'sort colors', 'valid palindrome'
        ],
        
        'binary-search': [
            'binary search', 'search in rotated', 'find minimum', 'find peak', 'search for range',
            'first bad version', 'sqrt', 'search a 2d matrix', 'median of two sorted arrays'
        ],
        
        'graph': [
            'graph', 'islands', 'number of islands', 'surrounded regions', 'clone graph', 
            'course schedule', 'word ladder', 'network delay time', 'cheapest flights'
        ],
        
        'depth-first-search': [
            'dfs', 'depth first', 'islands', 'path sum', 'validate binary search tree',
            'symmetric tree', 'invert binary tree'
        ],
        
        'breadth-first-search': [
            'bfs', 'breadth first', 'level order', 'minimum depth', 'binary tree level order'
        ],
        
        'backtracking': [
            'permutation', 'combination', 'subset', 'generate parentheses', 'letter combinations',
            'word search', 'n queens', 'sudoku solver', 'palindrome partitioning',
            'maximum bitwise or', 'letter tile possibilities'
        ],
        
        'greedy': [
            'greedy', 'jump game', 'gas station', 'candy', 'meeting rooms', 'interval'
        ],
        
        'bit-manipulation': [
            'bit manipulation', 'single number', 'counting bits', 'reverse bits', 
            'number of 1 bits', 'bitwise', 'power of two', 'reordered power of 2',
            'maximum bitwise or'
        ],
        
        'heap': [
            'heap', 'priority queue', 'top k', 'kth largest', 'kth smallest', 'merge k sorted',
            'sliding window maximum', 'find median', 'k closest points'
        ],
        
        'trie': [
            'trie', 'prefix tree', 'implement trie', 'word search', 'auto complete'
        ],
        
        'sliding-window': [
            'sliding window', 'minimum window', 'longest substring', 'max consecutive',
            'fruit into baskets', 'fruits into baskets', 'minimum size subarray'
        ],
        
        'sorting': [
            'sort', 'merge sort', 'quick sort', 'heap sort', 'bucket sort', 'radix sort',
            'sort array', 'sort colors', 'sort array by parity'
        ],
        
        'design': [
            'design', 'implement', 'task manager', 'data structure', 'iterator'
        ]
    }
    
    # Check each category for matches
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in title_lower:
                return category
    
    # Fallback to array for unknown problems
    return 'array'


def create_directory_structure():
    """Create directory structure based on LeetCode's official categories."""
    # Official LeetCode categories (most commonly used)
    categories = [
        'array', 'string', 'hash-table', 'dynamic-programming', 'math', 'sorting',
        'greedy', 'depth-first-search', 'binary-search', 'tree', 'breadth-first-search',
        'two-pointers', 'bit-manipulation', 'stack', 'heap', 'backtracking',
        'linked-list', 'sliding-window', 'graph', 'design', 'trie'
    ]
    
    difficulties = ['easy', 'medium', 'hard']
    
    for category in categories:
        for difficulty in difficulties:
            os.makedirs(f"{category}/{difficulty}", exist_ok=True)
            print(f"Created directory: {category}/{difficulty}")


def organize_solutions(problem_dir, new_dir):
    """Organize multiple solutions for a problem, preserving all versions."""
    # Skip if source and destination are the same
    if problem_dir.resolve() == new_dir.resolve():
        solution_count = len([f for f in problem_dir.iterdir() if f.name.endswith('.py')])
        print(f"  📁 Already in correct location ({solution_count} solution(s))")
        return solution_count
    
    # Copy the problem statement
    txt_file = None
    for file in problem_dir.iterdir():
        if file.name.endswith('.txt'):
            txt_file = file
            break
    
    if txt_file and not (new_dir / txt_file.name).exists():
        shutil.copy2(txt_file, new_dir / txt_file.name)
        print(f"  📄 Copied problem statement: {txt_file.name}")
    
    # Copy all solution files (multiple solutions)
    solution_count = 0
    for file in problem_dir.iterdir():
        if file.name.endswith('.py'):
            dest_file = new_dir / file.name
            if not dest_file.exists():
                shutil.copy2(file, dest_file)
                solution_count += 1
            else:
                solution_count += 1  # Count existing files
    
    print(f"  💡 Organized {solution_count} solution(s)")
    return solution_count


def main():
    """Main reorganization function."""
    print("🚀 Starting LeetCode repository reorganization with official categories...")
    
    # Get current directory
    current_dir = Path('.')
    
    # Create new directory structure
    print("\n📁 Creating official LeetCode category structure...")
    create_directory_structure()
    
    # Statistics
    total_problems = 0
    category_stats = {}
    difficulty_stats = {}
    solution_stats = {'total_solutions': 0, 'multi_solution_problems': 0}
    
    # Process each existing category directory
    for item in current_dir.iterdir():
        if not item.is_dir() or item.name.startswith('.') or item.name in ['__pycache__']:
            continue
            
        category_dir = item
        if category_dir.name in ['array-string', 'linked-list', 'tree', 'dynamic-programming', 
                                'graph', 'binary-search', 'heap', 'trie', 'backtracking', 
                                'math-bit', 'sliding-window', 'two-pointers']:
            
            print(f"\n🔍 Processing category: {category_dir.name}")
            
            # Process difficulty subdirectories
            for difficulty_dir in category_dir.iterdir():
                if not difficulty_dir.is_dir():
                    continue
                    
                print(f"  📊 Processing difficulty: {difficulty_dir.name}")
                
                # Process each problem
                for problem_dir in difficulty_dir.iterdir():
                    if not problem_dir.is_dir():
                        continue
                        
                    # Extract problem info from directory name
                    problem_name = problem_dir.name
                    print(f"    🔄 Processing: {problem_name}")
                    
                    # Try to read problem statement to get title
                    txt_file = problem_dir / f"{problem_name}.txt"
                    title = problem_name.replace('-', ' ')
                    number = re.match(r'(\d+)', problem_name)
                    number = number.group(1) if number else '0'
                    
                    if txt_file.exists():
                        try:
                            with open(txt_file, 'r', encoding='utf-8') as f:
                                content = f.read()
                                # Extract title from content if possible
                                title_match = re.search(r'(?:Problem\s+\d+[:\s]+)?(.*?)(?:\n|$)', content)
                                if title_match:
                                    title = title_match.group(1).strip()
                        except:
                            pass
                    
                    # Categorize based on old category and LeetCode official categories
                    new_category = map_old_to_new_category(category_dir.name, title, number)
                    difficulty = difficulty_dir.name
                    
                    # Create new directory path
                    new_dir = Path(f"{new_category}/{difficulty}/{problem_name}")
                    new_dir.mkdir(parents=True, exist_ok=True)
                    
                    # Organize solutions (handles multiple solutions)
                    solution_count = organize_solutions(problem_dir, new_dir)
                    
                    # Update statistics
                    total_problems += 1
                    category_stats[new_category] = category_stats.get(new_category, 0) + 1
                    difficulty_stats[difficulty] = difficulty_stats.get(difficulty, 0) + 1
                    solution_stats['total_solutions'] += solution_count
                    if solution_count > 1:
                        solution_stats['multi_solution_problems'] += 1
                    
                    print(f"    ✅ Moved to: {new_category}/{difficulty}/{problem_name}")
    
    # Print final statistics
    print(f"\n🎉 Reorganization complete!")
    print(f"\n📊 STATISTICS:")
    print(f"Total problems reorganized: {total_problems}")
    print(f"Total solution files: {solution_stats['total_solutions']}")
    print(f"Problems with multiple solutions: {solution_stats['multi_solution_problems']}")
    
    print(f"\n📈 Problems by Official LeetCode Category:")
    for category, count in sorted(category_stats.items()):
        print(f"  {category}: {count} problems")
    
    print(f"\n📊 Problems by Difficulty:")
    for difficulty, count in sorted(difficulty_stats.items()):
        print(f"  {difficulty}: {count} problems")


if __name__ == "__main__":
    main()