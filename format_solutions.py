#!/usr/bin/env python3
"""
LeetCode Solution Formatter

This script adds consistent headers to all exported Python solution files,
including placeholders for time and space complexity analysis.

Usage:
    python format_solutions.py

The script will:
1. Find all .py files in the current directory and subdirectories
2. Add a structured docstring header with problem information
3. Preserve the original solution code
4. Add placeholders for complexity analysis
"""

import os
import re
from pathlib import Path


def extract_problem_info(filename):
    """Extract problem information from filename."""
    # Convert filename to problem title
    name_without_ext = filename[:-3] if filename.endswith('.py') else filename
    
    # Replace hyphens with spaces and capitalize words
    title = name_without_ext.replace('-', ' ').replace('_', ' ')
    title = ' '.join(word.capitalize() for word in title.split())
    
    return title


def format_solution_file(filepath):
    """Format a single solution file with consistent header."""
    try:
        with open(filepath, "r", encoding='utf-8') as f:
            content = f.read().strip()
        
        # Skip if already formatted (contains our header pattern)
        if '"""' in content and 'Time Complexity:' in content:
            print(f"⏭️  Skipping {filepath.name} (already formatted)")
            return False
        
        # Skip if file is empty or doesn't contain a class Solution
        if not content or 'class Solution' not in content:
            print(f"⏭️  Skipping {filepath.name} (no Solution class found)")
            return False
        
        # Extract problem title from filename
        problem_title = extract_problem_info(filepath.name)
        
        # Try to extract problem description or number if present in original content
        problem_info = ""
        lines = content.split('\n')
        
        # Look for problem number patterns in comments
        for line in lines[:10]:  # Check first 10 lines
            line = line.strip()
            if line.startswith('#') or line.startswith('"""') or line.startswith("'''"):
                # Look for problem number pattern like "#1. Two Sum" or "Problem 1:"
                number_match = re.search(r'(?:problem\s*|#)?(\d+)(?:\.|:)?\s*(.+)', line.lower())
                if number_match:
                    number = number_match.group(1)
                    desc = number_match.group(2).strip(' #"\'')
                    if desc and len(desc) > 3:  # Basic validation
                        problem_info = f"LeetCode #{number}: {desc.capitalize()}"
                        break
        
        if not problem_info:
            problem_info = f"LeetCode: {problem_title}"
        
        # Find where class Solution starts
        class_match = re.search(r'^(.*?)(class Solution.*)', content, re.DOTALL | re.MULTILINE)
        if not class_match:
            print(f"⚠️  Warning: Could not find 'class Solution' in {filepath.name}")
            return False
        
        prefix_content = class_match.group(1).strip()
        solution_code = class_match.group(2)
        
        # Create the formatted header
        header = f'"""\n{problem_info}\n\n'
        
        # Add original problem context if there was any
        if prefix_content and not prefix_content.startswith('"""'):
            # Clean up the prefix content
            clean_prefix = '\n'.join(line.strip(' #"\'') for line in prefix_content.split('\n') if line.strip())
            if clean_prefix:
                header += f"Problem:\n{clean_prefix}\n\n"
        
        header += 'Algorithm:\n'
        header += 'TODO: Describe your approach here\n\n'
        header += 'Time Complexity: O(?)\n'
        header += 'Space Complexity: O(?)\n'
        header += '"""\n\n'
        
        # Combine header with solution
        formatted_content = header + solution_code
        
        # Write back to file
        with open(filepath, "w", encoding='utf-8') as f:
            f.write(formatted_content)
        
        print(f"✅ Formatted {filepath.name}")
        return True
        
    except Exception as e:
        print(f"❌ Error formatting {filepath.name}: {e}")
        return False


def main():
    """Main function to format all solution files."""
    print("🎨 LeetCode Solution Formatter")
    print("==============================")
    print()
    
    current_dir = Path(".")
    python_files = list(current_dir.rglob("*.py"))
    
    # Filter out this script itself
    script_name = Path(__file__).name
    python_files = [f for f in python_files if f.name != script_name]
    
    if not python_files:
        print("ℹ️  No Python files found to format.")
        return
    
    print(f"📁 Found {len(python_files)} Python files")
    print()
    
    formatted_count = 0
    
    for py_file in sorted(python_files):
        if format_solution_file(py_file):
            formatted_count += 1
    
    print()
    print(f"🎉 Formatting complete!")
    print(f"📊 {formatted_count} files were formatted")
    
    if formatted_count > 0:
        print()
        print("✨ Your solutions now have:")
        print("   • Consistent headers with problem information")
        print("   • Placeholders for time/space complexity analysis")
        print("   • Clean, interview-ready format")
        print()
        print("💡 Next steps:")
        print("   1. Review each file and fill in the complexity analysis")
        print("   2. Add algorithm descriptions where marked with TODO")
        print("   3. Commit your changes: git add . && git commit -m 'Format solutions with headers'")


if __name__ == "__main__":
    main()