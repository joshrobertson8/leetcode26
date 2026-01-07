#!/usr/bin/env python3
"""
LeetCode Repository Reorganizer

This script will:
1. Convert HTML problem statements from .md to plain text .txt files
2. Reorganize problems by category (Arrays & Strings, Trees, etc.) and difficulty
3. Move all solution files to the new structure
"""

import os
import re
import shutil
from pathlib import Path
from html import unescape
import html2text


def html_to_text(html_content):
    """Convert HTML content to plain text."""
    # Create html2text converter
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True
    h.ignore_emphasis = False
    h.body_width = 0  # Don't wrap lines
    
    # Convert HTML to markdown first, then clean up
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


def categorize_problem(title, number):
    """Categorize a problem based on its title and common patterns."""
    title_lower = title.lower()
    number_int = int(number) if number.isdigit() else 0
    
    # Define categories based on common patterns and known problems
    categories = {
        'array-string': [
            'array', 'string', 'two sum', 'palindrome', 'anagram', 'substring', 'subarray',
            'prefix', 'suffix', 'contains duplicate', 'merge', 'rotate', 'remove element',
            'remove duplicates', 'plus one', 'majority element', 'roman', 'longest common',
            'valid parentheses', 'search insert', 'length of last word', 'zigzag conversion',
            'container with most water', 'group anagrams', 'word pattern', 'isomorphic',
            'ransom note', 'is subsequence', 'product of array', 'merge intervals',
            'jump game', 'h-index', 'gas station', 'candy', 'find the index', 'simplify path'
        ],
        'linked-list': [
            'linked list', 'merge two sorted lists', 'reverse linked list', 'middle of',
            'cycle', 'intersection', 'palindrome linked list', 'swap nodes', 'remove nth',
            'add two numbers', 'delete', 'split'
        ],
        'tree': [
            'tree', 'binary tree', 'depth', 'height', 'invert', 'symmetric', 'path sum',
            'balanced', 'diameter', 'lowest common ancestor', 'serialize', 'deserialize',
            'level order', 'preorder', 'inorder', 'postorder', 'traversal'
        ],
        'dynamic-programming': [
            'climbing stairs', 'fibonacci', 'house robber', 'coin change', 'longest increasing',
            'edit distance', 'unique paths', 'minimum path sum', 'decode ways', 'word break',
            'longest palindromic substring', 'palindrome partitioning', 'best time to buy',
            'maximum subarray', 'range sum query', 'paint house', 'delete and earn',
            'min cost climbing stairs', 'partition equal subset sum'
        ],
        'graph': [
            'graph', 'islands', 'surrounded regions', 'clone graph', 'course schedule',
            'word ladder', 'network delay time', 'cheapest flights', 'union find',
            'topological sort', 'shortest path', 'minimum spanning tree'
        ],
        'binary-search': [
            'binary search', 'search in rotated', 'find minimum', 'find peak', 'search for range',
            'first bad version', 'sqrt', 'search a 2d matrix', 'median of two sorted arrays',
            'kth smallest', 'kth largest'
        ],
        'heap': [
            'heap', 'priority queue', 'top k', 'kth largest', 'kth smallest', 'merge k sorted',
            'sliding window maximum', 'find median', 'ugly number'
        ],
        'trie': [
            'trie', 'prefix tree', 'word search', 'auto complete', 'replace words'
        ],
        'backtracking': [
            'permutation', 'combination', 'subset', 'generate parentheses', 'letter combinations',
            'word search', 'n queens', 'sudoku solver', 'palindrome partitioning'
        ],
        'math-bit': [
            'power of', 'factorial', 'prime', 'gcd', 'lcm', 'bit manipulation', 'single number',
            'counting bits', 'reverse bits', 'number of 1 bits', 'bitwise', 'happy number',
            'ugly number', 'perfect square', 'integer to roman', 'excel sheet'
        ],
        'sliding-window': [
            'sliding window', 'minimum window', 'longest substring', 'max consecutive',
            'fruit into baskets', 'longest subarray', 'minimum size subarray'
        ],
        'two-pointers': [
            'two pointers', 'three sum', 'four sum', 'trapping rain water', 'container with most water',
            'remove duplicates', 'move zeroes', 'sort colors', 'minimum window substring'
        ]
    }
    
    # Check each category
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in title_lower:
                return category
    
    # Special number-based categorization for known problem ranges
    if 1 <= number_int <= 300:
        if any(keyword in title_lower for keyword in ['tree', 'binary tree']):
            return 'tree'
        elif any(keyword in title_lower for keyword in ['linked list']):
            return 'linked-list'
        elif any(keyword in title_lower for keyword in ['dynamic', 'dp', 'climb', 'robber']):
            return 'dynamic-programming'
    
    # Default fallback
    return 'array-string'


def create_directory_structure():
    """Create the new category/difficulty directory structure."""
    categories = [
        'array-string', 'linked-list', 'tree', 'dynamic-programming', 'graph',
        'binary-search', 'heap', 'trie', 'backtracking', 'math-bit',
        'sliding-window', 'two-pointers'
    ]
    
    difficulties = ['easy', 'medium', 'hard']
    
    for category in categories:
        for difficulty in difficulties:
            path = Path(category) / difficulty
            path.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {path}")


def process_problem(problem_dir):
    """Process a single problem directory."""
    problem_path = Path(problem_dir)
    
    # Find the markdown file
    md_files = list(problem_path.glob('*.md'))
    if not md_files:
        print(f"No .md file found in {problem_dir}")
        return None
    
    md_file = md_files[0]
    
    # Read the markdown content
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except Exception as e:
        print(f"Error reading {md_file}: {e}")
        return None
    
    # Extract difficulty, number, and title
    difficulty, number, title = extract_difficulty_and_title(html_content)
    
    # Categorize the problem
    category = categorize_problem(title, number)
    
    # Convert HTML to plain text
    plain_text = html_to_text(html_content)
    
    # Create the target directory
    target_dir = Path(category) / difficulty / problem_path.name
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # Write the plain text problem statement
    problem_file = target_dir / f"{problem_path.name}.txt"
    try:
        with open(problem_file, 'w', encoding='utf-8') as f:
            f.write(plain_text)
        print(f"Created: {problem_file}")
    except Exception as e:
        print(f"Error writing {problem_file}: {e}")
        return None
    
    # Copy all Python solution files
    py_files = list(problem_path.glob('*.py'))
    for py_file in py_files:
        target_py = target_dir / py_file.name
        try:
            shutil.copy2(py_file, target_py)
            print(f"Copied: {py_file} -> {target_py}")
        except Exception as e:
            print(f"Error copying {py_file}: {e}")
    
    return {
        'category': category,
        'difficulty': difficulty,
        'number': number,
        'title': title,
        'original_path': str(problem_path),
        'new_path': str(target_dir)
    }


def main():
    """Main function to reorganize the repository."""
    print("🔄 Starting LeetCode repository reorganization...")
    print()
    
    # Create directory structure
    print("📁 Creating category/difficulty directory structure...")
    create_directory_structure()
    print()
    
    # Get all problem directories
    current_dir = Path('.')
    problem_dirs = [d for d in current_dir.iterdir() 
                   if d.is_dir() and not d.name.startswith('.') and 
                   not d.name in ['README.md', 'debug.log', 'export_basic.sh', 
                                  'export_grouped.sh', 'format_solutions.py', 'setup_repo.sh']]
    
    # Filter to only directories that look like problem directories (contain numbers)
    problem_dirs = [d for d in problem_dirs if re.match(r'^\d+', d.name)]
    
    print(f"📊 Found {len(problem_dirs)} problem directories to process...")
    print()
    
    # Process each problem
    results = []
    for problem_dir in sorted(problem_dirs):
        print(f"Processing: {problem_dir.name}")
        result = process_problem(problem_dir)
        if result:
            results.append(result)
        print()
    
    # Generate summary report
    print("📈 Reorganization Summary:")
    print("=" * 50)
    
    # Count by category
    category_counts = {}
    difficulty_counts = {}
    
    for result in results:
        category = result['category']
        difficulty = result['difficulty']
        
        category_counts[category] = category_counts.get(category, 0) + 1
        difficulty_counts[difficulty] = difficulty_counts.get(difficulty, 0) + 1
    
    print("\nProblems by Category:")
    for category, count in sorted(category_counts.items()):
        print(f"  {category}: {count} problems")
    
    print("\nProblems by Difficulty:")
    for difficulty, count in sorted(difficulty_counts.items()):
        print(f"  {difficulty}: {count} problems")
    
    print(f"\nTotal problems reorganized: {len(results)}")
    print()
    print("✅ Reorganization complete!")
    print()
    print("📝 Next steps:")
    print("1. Review the new structure")
    print("2. Remove old problem directories if everything looks correct")
    print("3. Update your README.md to reflect the new organization")
    print("4. Commit the changes to Git")


if __name__ == "__main__":
    main()