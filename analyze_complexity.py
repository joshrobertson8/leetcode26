#!/usr/bin/env python3
"""
Complexity Analyzer for LeetCode Solutions

Automatically analyzes Python solutions and generates:
- Time/Space complexity
"""

import ast
import re
from pathlib import Path
from typing import Tuple
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
        self.nested_depth += 1
        self.max_nested_depth = max(self.max_nested_depth, self.nested_depth)
        
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
        self.nested_depth += 1
        self.max_nested_depth = max(self.max_nested_depth, self.nested_depth)
        
        self.loops.append({
            'type': 'while',
            'nested': self.nested_depth
        })
        
        self.generic_visit(node)
        self.nested_depth -= 1
    
    def visit_Call(self, node):
        func_name = self._get_func_name(node.func)
        
        if func_name:
            self.function_calls.append(func_name)
            
            if func_name in ['sorted', 'sort']:
                self.has_sort = True
            elif 'bisect' in func_name.lower():
                self.has_binary_search = True
        
        self.generic_visit(node)
    
    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                var_name = target.id.lower()
                
                if isinstance(node.value, ast.Dict):
                    self.data_structures['dict'] += 1
                    self.has_hash_store = True
                elif isinstance(node.value, ast.Set):
                    self.data_structures['set'] += 1
                    self.has_hash_store = True
                elif isinstance(node.value, ast.List):
                    self.data_structures['list'] += 1
                elif isinstance(node.value, ast.Call):
                    func_name = self._get_func_name(node.value.func)
                    if func_name in ['dict', 'set', 'defaultdict', 'Counter']:
                        self.data_structures['dict'] += 1
                        self.has_hash_store = True
        
        self.generic_visit(node)
    
    def visit_Subscript(self, node):
        if isinstance(node.value, ast.Name):
            var_name = node.value.id.lower()
            if any(keyword in var_name for keyword in ['dict', 'hash', 'map', 'seen', 'visited', 'set']):
                self.has_hash_lookup = True
        
        self.generic_visit(node)
    
    def visit_Compare(self, node):
        for op in node.ops:
            if isinstance(op, ast.In):
                for comparator in node.comparators:
                    if isinstance(comparator, ast.Name):
                        var_name = comparator.id.lower()
                        if any(keyword in var_name for keyword in ['dict', 'hash', 'map', 'seen', 'visited', 'set']):
                            self.has_hash_lookup = True
        self.generic_visit(node)
    
    def visit_FunctionDef(self, node):
        func_name = node.name
        for child in ast.walk(node):
            if isinstance(child, ast.Call) and isinstance(child.func, ast.Name):
                if child.func.id == func_name:
                    self.recursive_calls.append(func_name)
        self.generic_visit(node)
    
    def _get_iter_type(self, node):
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
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return node.attr
        return None
    
    def analyze(self, code: str) -> Tuple[str, str]:
        try:
            tree = ast.parse(code)
            self.visit(tree)
            return self._determine_complexity()
        except Exception:
            return "O(?)", "O(?)"
    
    def _determine_complexity(self) -> Tuple[str, str]:
        time = self._analyze_time_complexity()
        space = self._analyze_space_complexity()
        return time, space
    
    def _analyze_time_complexity(self) -> str:
        if self.has_sort:
            return "O(n log n)"
        
        if self.has_binary_search:
            if self.max_nested_depth >= 1:
                return "O(n log n)"
            return "O(log n)"
        
        if self.max_nested_depth >= 2:
            return "O(n^2)"
        
        if self.max_nested_depth == 1:
            return "O(n)"
        
        if self.recursive_calls:
            return "O(n)"
        
        return "O(1)"
    
    def _analyze_space_complexity(self) -> str:
        if self.recursive_calls:
            return "O(n)"
        
        if self.data_structures['dict'] > 0 or self.data_structures['set'] > 0:
            return "O(n)"
        
        if self.data_structures['list'] > 0:
            if len(self.array_creations) > 0 or len(self.loops) > 0:
                return "O(n)"
        
        return "O(1)"


def analyze_solution_file(file_path: Path) -> Tuple[str, str]:
    """Analyze a single solution file and return complexities."""
    try:
        content = file_path.read_text(encoding="utf-8")
        lines = content.split('\n')
        code_start = 0
        
        # First priority: find "class Solution" at the start of a line
        for i, line in enumerate(lines):
            if line.startswith('class Solution'):
                code_start = i
                break
        
        # Second priority: find any class at start of line after docstring closes
        if code_start == 0:
            docstring_end = 0
            docstring_count = 0
            for i, line in enumerate(lines):
                docstring_count += line.count('"""')
                if docstring_count >= 2:  # Found opening and closing
                    docstring_end = i
                    break
            
            for i in range(docstring_end, len(lines)):
                if lines[i].startswith('class '):
                    code_start = i
                    break
        
        # Third priority: any line starting with class
        if code_start == 0:
            for i, line in enumerate(lines):
                if line.startswith('class '):
                    code_start = i
                    break
        
        code = '\n'.join(lines[code_start:])
        
        # Analyze complexity
        analyzer = ComplexityAnalyzer()
        time, space = analyzer.analyze(code)
        
        return time, space
    except Exception:
        return "O(?)", "O(?)"


def update_solution_file(file_path: Path, time_complexity: str, space_complexity: str):
    """Update the complexity in a solution file."""
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
        
        file_path.write_text(content, encoding="utf-8")
        return True
    except Exception:
        return False


def analyze_all_solutions():
    """Analyze all solution files in the repository."""
    print("=" * 70)
    print("LeetCode Solution Complexity Analyzer")
    print("=" * 70)
    print()
    
    solution_files = []
    
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
        
        time_comp, space_comp = analyze_solution_file(file_path)
        
        if time_comp != "O(?)" or space_comp != "O(?)":
            if update_solution_file(file_path, time_comp, space_comp):
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
