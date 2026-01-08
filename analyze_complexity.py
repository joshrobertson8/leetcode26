#!/usr/bin/env python3
"""
Complexity Analyzer for LeetCode Solutions

Automatically analyzes Python solutions and updates time/space complexity.
Uses AST parsing and pattern recognition to determine Big O complexity.
"""

import ast
import re
from pathlib import Path
from typing import Dict, List, Tuple, Set, Optional
from collections import defaultdict

BASE_DIR = Path(__file__).parent


class ComplexityAnalyzer(ast.NodeVisitor):
    """AST visitor to analyze code complexity."""
    
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.loops = []
        self.recursive_calls = []
        self.data_structures = defaultdict(int)
        self.nested_depth = 0
        self.max_nested_depth = 0
        self.has_sort = False
        self.has_binary_search = False
        self.has_hash_lookup = False
        self.has_hash_store = False
        self.loop_vars = set()
        self.array_creations = []
        self.function_calls = []
        
    def visit_For(self, node):
        """Analyze for loops."""
        self.nested_depth += 1
        self.max_nested_depth = max(self.max_nested_depth, self.nested_depth)
        
        # Track loop variable
        if isinstance(node.target, ast.Name):
            self.loop_vars.add(node.target.id)
        
        iter_type = self._get_iter_type(node.iter)
        self.loops.append({
            'type': 'for',
            'iter_type': iter_type,
            'nested': self.nested_depth,
            'target': node.target.id if isinstance(node.target, ast.Name) else None
        })
        
        self.generic_visit(node)
        self.nested_depth -= 1
    
    def visit_While(self, node):
        """Analyze while loops."""
        self.nested_depth += 1
        self.max_nested_depth = max(self.max_nested_depth, self.nested_depth)
        
        self.loops.append({
            'type': 'while',
            'nested': self.nested_depth
        })
        
        self.generic_visit(node)
        self.nested_depth -= 1
    
    def visit_Call(self, node):
        """Analyze function calls."""
        func_name = self._get_func_name(node.func)
        
        if func_name:
            self.function_calls.append(func_name)
            
            if func_name in ['sorted', 'sort']:
                self.has_sort = True
            elif 'bisect' in func_name.lower():
                self.has_binary_search = True
            elif func_name in ['min', 'max'] and len(node.args) > 0:
                # min/max on iterable could be O(n)
                pass
        
        self.generic_visit(node)
    
    def visit_Assign(self, node):
        """Track variable assignments and data structures."""
        for target in node.targets:
            if isinstance(target, ast.Name):
                var_name = target.id.lower()
                
                # Check for hash table creation
                if isinstance(node.value, ast.Dict):
                    self.data_structures['dict'] += 1
                    self.has_hash_store = True
                elif isinstance(node.value, ast.Set):
                    self.data_structures['set'] += 1
                    self.has_hash_store = True
                elif isinstance(node.value, ast.List):
                    self.data_structures['list'] += 1
                    # Check if creating array of size n
                    if isinstance(node.value, ast.ListComp) or \
                       (isinstance(node.value, ast.Call) and 
                        self._get_func_name(node.value.func) in ['list', 'range']):
                        self.array_creations.append(var_name)
                elif isinstance(node.value, ast.Call):
                    func_name = self._get_func_name(node.value.func)
                    if func_name in ['dict', '{}', 'set', 'defaultdict', 'Counter']:
                        self.data_structures['dict'] += 1
                        self.has_hash_store = True
                    elif func_name in ['list', '[]', 'range']:
                        self.data_structures['list'] += 1
        
        self.generic_visit(node)
    
    def visit_Subscript(self, node):
        """Analyze dictionary/list access."""
        if isinstance(node.value, ast.Name):
            var_name = node.value.id.lower()
            if any(keyword in var_name for keyword in ['dict', 'hash', 'map', 'seen', 'visited', 'set']):
                self.has_hash_lookup = True
        
        self.generic_visit(node)
    
    def visit_Dict(self, node):
        """Track dictionary usage."""
        self.data_structures['dict'] += 1
        self.has_hash_store = True
        self.generic_visit(node)
    
    def visit_Set(self, node):
        """Track set usage."""
        self.data_structures['set'] += 1
        self.has_hash_store = True
        self.generic_visit(node)
    
    def visit_List(self, node):
        """Track list usage."""
        self.data_structures['list'] += 1
        self.generic_visit(node)
    
    def visit_Compare(self, node):
        """Check for 'in' operator (hash lookup)."""
        for op in node.ops:
            if isinstance(op, ast.In):
                # Check if checking in dict/set
                for comparator in node.comparators:
                    if isinstance(comparator, ast.Name):
                        var_name = comparator.id.lower()
                        if any(keyword in var_name for keyword in ['dict', 'hash', 'map', 'seen', 'visited', 'set']):
                            self.has_hash_lookup = True
        self.generic_visit(node)
    
    def visit_FunctionDef(self, node):
        """Track recursive calls."""
        func_name = node.name
        for child in ast.walk(node):
            if isinstance(child, ast.Call) and isinstance(child.func, ast.Name):
                if child.func.id == func_name:
                    self.recursive_calls.append(func_name)
        self.generic_visit(node)
    
    def _get_iter_type(self, node):
        """Determine what we're iterating over."""
        if isinstance(node, ast.Call):
            func_name = self._get_func_name(node.func)
            if func_name == 'range':
                return 'range(n)'
            elif func_name == 'enumerate':
                return 'enumerate(n)'
            elif func_name == 'zip':
                return 'zip(n)'
        elif isinstance(node, ast.Name):
            return 'variable'
        return 'unknown'
    
    def _get_func_name(self, node):
        """Extract function name from AST node."""
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return node.attr
        return None
    
    def analyze(self, code: str) -> Tuple[str, str]:
        """Analyze code and return time/space complexity."""
        try:
            tree = ast.parse(code)
            self.visit(tree)
            return self._determine_complexity()
        except Exception:
            return "O(?)", "O(?)"
    
    def _determine_complexity(self) -> Tuple[str, str]:
        """Determine time and space complexity based on analysis."""
        # Time complexity analysis
        time = self._analyze_time_complexity()
        
        # Space complexity analysis
        space = self._analyze_space_complexity()
        
        return time, space
    
    def _analyze_time_complexity(self) -> str:
        """Determine time complexity."""
        # Check for sorting
        if self.has_sort:
            if self.max_nested_depth >= 1:
                return "O(n log n)"
            return "O(n log n)"
        
        # Check for binary search
        if self.has_binary_search:
            if self.max_nested_depth >= 1:
                return "O(n log n)"  # Binary search in loop
            return "O(log n)"
        
        # Nested loops
        if self.max_nested_depth >= 2:
            return "O(n²)"
        
        # Single loop
        if self.max_nested_depth == 1:
            # Check if hash lookup in loop (Two Sum pattern)
            if self.has_hash_lookup:
                return "O(n)"  # Hash lookup is O(1)
            return "O(n)"
        
        # No loops - check for recursion
        if self.recursive_calls:
            # Could be O(2^n) for backtracking or O(n) for simple recursion
            # Default to O(n) unless we see exponential patterns
            return "O(n)"
        
        # Simple operations
        return "O(1)"
    
    def _analyze_space_complexity(self) -> str:
        """Determine space complexity."""
        # Check for recursion (call stack)
        if self.recursive_calls:
            if self.data_structures['dict'] > 0 or self.data_structures['set'] > 0:
                return "O(n)"  # Both call stack and hash table
            return "O(n)"  # Call stack
        
        # Hash tables/sets
        if self.data_structures['dict'] > 0 or self.data_structures['set'] > 0:
            if self.has_hash_store or self.has_hash_lookup:
                return "O(n)"  # Storing up to n elements
        
        # Arrays/lists
        if self.data_structures['list'] > 0:
            if len(self.array_creations) > 0 or len(self.loops) > 0:
                return "O(n)"  # Creating arrays of size n
        
        # No extra space
        return "O(1)"


def generate_algorithm_description(content: str, code: str) -> str:
    """Generate algorithm description based on code analysis."""
    content_lower = content.lower()
    code_lower = code.lower()
    
    # Pattern-based descriptions
    descriptions = []
    
    # Hash table patterns
    if any(keyword in code_lower for keyword in ['hash', 'dict', '{}', 'seen', 'visited']):
        if 'in ' in code and 'for' in code:
            descriptions.append("Use a hash table to store seen elements for O(1) lookup")
    
    # Two pointers
    if 'left' in code_lower and 'right' in code_lower and 'while' in code_lower:
        descriptions.append("Two pointers technique")
    elif 'left' in code_lower and 'right' in code_lower:
        descriptions.append("Two pointers approach")
    
    # Sliding window
    if 'window' in code_lower or ('left' in code_lower and 'right' in code_lower and 'while' in code_lower):
        descriptions.append("Sliding window technique")
    
    # Prefix/suffix arrays
    if 'prefix' in code_lower or 'suffix' in code_lower:
        if 'prefix' in code_lower:
            descriptions.append("Build prefix array")
        if 'suffix' in code_lower:
            descriptions.append("Build suffix array")
    
    # Product except self pattern
    if 'product' in content_lower and 'except' in content_lower:
        if code.count('for') == 2:
            descriptions.append("Two-pass approach: first pass calculates prefix products, second pass multiplies by suffix products")
    
    # Trie
    if 'trie' in code_lower or 'trienode' in code_lower:
        descriptions.append("Trie data structure for efficient prefix matching")
    
    # Binary search
    if 'binary' in code_lower or 'bisect' in code_lower or ('left' in code_lower and 'right' in code_lower and 'mid' in code_lower):
        descriptions.append("Binary search algorithm")
    
    # Sorting
    if '.sort()' in code or 'sorted(' in code:
        descriptions.append("Sort the array first")
    
    # Backtracking/recursion
    if 'def ' in code and code.count('def ') > 1:
        # Check for recursive calls
        lines = code.split('\n')
        func_name = None
        for line in lines:
            if 'def ' in line and 'self.' not in line:
                func_name = line.split('def ')[1].split('(')[0].strip()
                break
        if func_name:
            for line in lines:
                if func_name + '(' in line and 'def ' not in line:
                    descriptions.append("Recursive backtracking approach")
                    break
    
    # Dynamic programming
    if 'dp' in code_lower or 'memo' in code_lower or 'cache' in code_lower:
        descriptions.append("Dynamic programming with memoization")
    
    # Greedy
    if 'max(' in code_lower or 'min(' in code_lower:
        if 'for' in code_lower:
            descriptions.append("Greedy algorithm")
    
    # Stack
    if 'stack' in code_lower or 'append' in code_lower and 'pop' in code_lower:
        if '[' in code and ']' in code:
            descriptions.append("Stack-based approach")
    
    # Queue/BFS
    if 'deque' in code_lower or 'queue' in code_lower:
        descriptions.append("BFS using queue")
    
    # DFS
    if 'dfs' in code_lower or ('def ' in code and 'visited' in code_lower):
        descriptions.append("DFS traversal")
    
    # If no specific pattern found, describe based on loops
    if not descriptions:
        if 'for' in code_lower and code.count('for') >= 2:
            descriptions.append("Nested loops to check all pairs")
        elif 'for' in code_lower:
            descriptions.append("Iterate through the array once")
        elif 'while' in code_lower:
            descriptions.append("Iterate until condition is met")
    
    # Default description
    if not descriptions:
        descriptions.append("Direct implementation")
    
    return ". ".join(descriptions) + "."


def analyze_solution_file(file_path: Path) -> Tuple[str, str, str]:
    """Analyze a single solution file and return complexities and description."""
    try:
        content = file_path.read_text(encoding="utf-8")
        
        # Extract code (skip docstring)
        lines = content.split('\n')
        code_start = 0
        
        # Find where class starts
        for i, line in enumerate(lines):
            if line.strip().startswith('class '):
                code_start = i
                break
        
        code = '\n'.join(lines[code_start:])
        
        # Special pattern matching for common algorithms
        time, space = _pattern_match_complexity(content)
        if time == "O(?)" or space == "O(?)":
            analyzer = ComplexityAnalyzer()
            time, space = analyzer.analyze(code)
        
        # Generate description
        description = generate_algorithm_description(content, code)
        
        return time, space, description
    except Exception:
        return "O(?)", "O(?)", "Algorithm implementation"


def _pattern_match_complexity(content: str) -> Tuple[str, str]:
    """Use pattern matching for common algorithms."""
    content_lower = content.lower()
    
    # Two Sum pattern - hash table lookup
    if 'hash' in content_lower and 'in ' in content and 'for' in content:
        if 'enumerate' in content or 'range(len' in content:
            return "O(n)", "O(n)"
    
    # Product Except Self - two passes
    if 'product' in content_lower and 'except' in content_lower:
        if content.count('for') == 2:
            return "O(n)", "O(1)"  # Usually O(1) space if using result array
    
    # Trie operations
    if 'trie' in content_lower or 'trienode' in content_lower:
        if 'insert' in content_lower or 'search' in content_lower:
            return "O(m)", "O(m)"  # m is word length
    
    # Binary search
    if 'binary' in content_lower or 'bisect' in content_lower:
        return "O(log n)", "O(1)"
    
    # Sorting
    if '.sort()' in content or 'sorted(' in content:
        if 'for' in content:
            return "O(n log n)", "O(1)" if 'in-place' in content_lower else "O(n)"
        return "O(n log n)", "O(n)"
    
    return "O(?)", "O(?)"


def update_solution_file(file_path: Path, time_complexity: str, space_complexity: str, description: str = None):
    """Update the complexity and algorithm description in a solution file."""
    try:
        content = file_path.read_text(encoding="utf-8")
        
        # Replace Time Complexity
        content = re.sub(
            r'Time Complexity:\s*O\([^)]*\)',
            f'Time Complexity: {time_complexity}',
            content
        )
        
        # Replace Space Complexity
        content = re.sub(
            r'Space Complexity:\s*O\([^)]*\)',
            f'Space Complexity: {space_complexity}',
            content
        )
        
        # Replace TODO with description
        if description:
            # Replace TODO: Describe your approach here
            content = re.sub(
                r'TODO:\s*Describe your approach here',
                description,
                content,
                flags=re.IGNORECASE
            )
            
            # Also replace just "TODO:" if it exists
            content = re.sub(
                r'Algorithm:\s*\n\s*TODO:.*?\n',
                f'Algorithm:\n{description}\n',
                content,
                flags=re.IGNORECASE | re.DOTALL
            )
        
        # If no complexity found, add it after Algorithm line
        if 'Time Complexity:' not in content:
            algo_match = re.search(r'Algorithm:\s*.*?\n', content, re.DOTALL)
            if algo_match:
                insert_pos = algo_match.end()
                content = content[:insert_pos] + f'\nTime Complexity: {time_complexity}\nSpace Complexity: {space_complexity}\n' + content[insert_pos:]
        
        file_path.write_text(content, encoding="utf-8")
        return True
    except Exception as e:
        return False


def analyze_all_solutions():
    """Analyze all solution files in the repository."""
    print("=" * 70)
    print("LeetCode Solution Complexity Analyzer")
    print("=" * 70)
    print()
    
    solution_files = []
    
    # Find all Python solution files
    for category_dir in BASE_DIR.iterdir():
        if not category_dir.is_dir() or category_dir.name.startswith('.'):
            continue
        
        for difficulty_dir in category_dir.iterdir():
            if not difficulty_dir.is_dir():
                continue
            
            for problem_dir in difficulty_dir.iterdir():
                if not problem_dir.is_dir():
                    continue
                
                for py_file in problem_dir.glob("*.py"):
                    if py_file.name.endswith('.py'):
                        solution_files.append(py_file)
    
    print(f"Found {len(solution_files)} solution files")
    print()
    
    updated = 0
    failed = 0
    
    for i, file_path in enumerate(solution_files, 1):
        rel_path = file_path.relative_to(BASE_DIR)
        print(f"[{i:4d}/{len(solution_files)}] {str(rel_path)[:50]:<50}", end=" ")
        
        time_comp, space_comp, description = analyze_solution_file(file_path)
        
        if time_comp != "O(?)" or space_comp != "O(?)":
            if update_solution_file(file_path, time_comp, space_comp, description):
                print(f"-> {time_comp:8s} / {space_comp:8s}")
                updated += 1
            else:
                print("-> FAILED")
                failed += 1
        else:
            print("-> SKIPPED")
            failed += 1
    
    print()
    print("=" * 70)
    print("Analysis Complete")
    print("=" * 70)
    print(f"Updated: {updated}")
    print(f"Failed: {failed}")
    print(f"Total: {len(solution_files)}")


if __name__ == "__main__":
    analyze_all_solutions()
