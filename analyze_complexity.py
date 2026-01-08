#!/usr/bin/env python3
"""
Complexity Analyzer for LeetCode Solutions

Automatically analyzes Python solutions and generates:
- Time/Space complexity
- Personalized algorithm descriptions based on actual code logic
"""

import ast
import re
from pathlib import Path
from typing import Dict, List, Tuple, Set, Optional
from collections import defaultdict

BASE_DIR = Path(__file__).parent


class AlgorithmDescriber(ast.NodeVisitor):
    """
    Generates personalized, plain-English descriptions of how the code works.
    Describes step by step what the algorithm does.
    """
    
    def __init__(self):
        self.steps = []
        self.data_structures = {}  # var_name -> description
        self.loop_patterns = []
        self.has_recursion = False
        self.recursive_func_name = None
        self.helper_funcs = []
        self.main_func_name = ""
        self.comparisons = []
        self.key_operations = []
        self.return_info = None
        self.uses_sorting = False
        self.uses_heap = False
        self.uses_stack = False
        self.uses_two_pointers = False
        self.uses_sliding_window = False
        self.uses_binary_search = False
        self.pointer_vars = set()
        self.uses_string_clean = False
        self.uses_reverse = False
        self.uses_join = False
        self.window_vars = set()
        
    def visit_FunctionDef(self, node):
        func_name = node.name
        
        # Skip dunder methods
        if func_name.startswith('__'):
            self.generic_visit(node)
            return
            
        # Track helper functions vs main function
        if not self.main_func_name:
            self.main_func_name = func_name
        elif func_name != self.main_func_name:
            self.helper_funcs.append(func_name)
            
        # Check for recursion
        for child in ast.walk(node):
            if isinstance(child, ast.Call):
                call_name = self._get_call_name(child)
                if call_name == func_name:
                    self.has_recursion = True
                    self.recursive_func_name = func_name
        
        self.generic_visit(node)
    
    def visit_Assign(self, node):
        """Analyze variable assignments to understand data structures used."""
        for target in node.targets:
            if isinstance(target, ast.Name):
                var_name = target.id
                var_lower = var_name.lower()
                
                # Check for pointer patterns
                if any(p in var_lower for p in ['left', 'right', 'lo', 'hi', 'start', 'end', 'prev', 'curr', 'next', 'fast', 'slow', 'head', 'tail']):
                    self.pointer_vars.add(var_name)
                    if len(self.pointer_vars) >= 2:
                        self.uses_two_pointers = True
                
                # Check for sliding window pattern
                if any(w in var_lower for w in ['left', 'right', 'window', 'basket', 'count']):
                    self.window_vars.add(var_name)
                
                # Check for reverse operation
                if isinstance(node.value, ast.Subscript):
                    if isinstance(node.value.slice, ast.Slice):
                        step = node.value.slice.step
                        if isinstance(step, ast.UnaryOp) and isinstance(step.op, ast.USub):
                            self.uses_reverse = True
                
                desc = self._describe_assignment(node.value, var_name)
                if desc:
                    self.data_structures[var_name] = desc
        
        self.generic_visit(node)
    
    def visit_For(self, node):
        """Analyze for loops."""
        loop_info = self._analyze_for_loop(node)
        if loop_info:
            self.loop_patterns.append(loop_info)
        self.generic_visit(node)
    
    def visit_While(self, node):
        """Analyze while loops."""
        loop_info = self._analyze_while_loop(node)
        if loop_info:
            self.loop_patterns.append(loop_info)
        self.generic_visit(node)
    
    def visit_Call(self, node):
        """Track important function calls."""
        call_name = self._get_call_name(node)
        
        if call_name:
            if call_name in ['sorted', 'sort']:
                self.uses_sorting = True
                self.key_operations.append('sort the input')
            elif call_name in ['heappush', 'heappop', 'heapify']:
                self.uses_heap = True
            elif call_name in ['append', 'pop'] and self._is_stack_usage(node):
                self.uses_stack = True
            elif 'bisect' in call_name.lower():
                self.uses_binary_search = True
            elif call_name == 'join':
                self.uses_join = True
            elif call_name in ['isalnum', 'isalpha', 'isdigit', 'lower', 'upper', 'strip']:
                self.uses_string_clean = True
                
        self.generic_visit(node)
    
    def visit_Return(self, node):
        """Analyze return statements."""
        if node.value:
            self.return_info = self._describe_return(node.value)
        self.generic_visit(node)
    
    def _get_call_name(self, node) -> Optional[str]:
        """Get the name of a function call."""
        if isinstance(node.func, ast.Name):
            return node.func.id
        elif isinstance(node.func, ast.Attribute):
            return node.func.attr
        return None
    
    def _describe_assignment(self, value_node, var_name: str) -> Optional[str]:
        """Describe what a variable assignment means."""
        var_lower = var_name.lower()
        
        if isinstance(value_node, ast.Dict):
            if any(k in var_lower for k in ['hash', 'map', 'table', 'seen', 'visited']):
                return "hash map to track seen values"
            elif 'count' in var_lower:
                return "hash map to count frequencies"
            elif 'bank' in var_lower or 'match' in var_lower:
                return "mapping for matching pairs"
            return "dictionary"
            
        elif isinstance(value_node, ast.Set):
            if 'seen' in var_lower or 'visited' in var_lower:
                return "set to track visited elements"
            return "set for O(1) lookup"
            
        elif isinstance(value_node, ast.List):
            if 'stack' in var_lower:
                self.uses_stack = True
                return "stack"
            elif 'result' in var_lower or 'res' in var_lower or 'ans' in var_lower:
                return "result list"
            return "list"
            
        elif isinstance(value_node, ast.Call):
            func_name = self._get_call_name(value_node)
            if func_name == 'defaultdict':
                return "defaultdict for grouping"
            elif func_name == 'Counter':
                return "Counter to count frequencies"
            elif func_name == 'deque':
                return "deque for BFS traversal"
            elif func_name == 'set':
                return "set for O(1) lookup"
            elif func_name == 'sorted':
                self.uses_sorting = True
                return "sorted copy of input"
                
        elif isinstance(value_node, ast.BinOp):
            if isinstance(value_node.op, ast.Mult):
                # [0] * n pattern
                if isinstance(value_node.left, ast.List):
                    return "array initialized with default values"
                    
        return None
    
    def _analyze_for_loop(self, node) -> Optional[str]:
        """Analyze a for loop and describe its purpose."""
        iter_node = node.iter
        
        if isinstance(iter_node, ast.Call):
            func_name = self._get_call_name(iter_node)
            
            if func_name == 'range':
                args = iter_node.args
                if len(args) >= 3:
                    # Check for reverse iteration
                    step = args[2]
                    if isinstance(step, ast.UnaryOp) and isinstance(step.op, ast.USub):
                        return "iterate backwards through the array"
                return "iterate through each index"
                
            elif func_name == 'enumerate':
                return "iterate through each element with its index"
                
            elif func_name == 'zip':
                return "iterate through multiple arrays in parallel"
                
            elif func_name == 'items':
                return "iterate through each key-value pair"
                
        elif isinstance(iter_node, ast.Name):
            var_name = iter_node.id.lower()
            if 'str' in var_name or var_name == 's':
                return "iterate through each character"
            return f"iterate through {iter_node.id}"
            
        elif isinstance(iter_node, ast.Attribute):
            if iter_node.attr == 'items':
                return "iterate through each key-value pair"
            elif iter_node.attr == 'keys':
                return "iterate through each key"
            elif iter_node.attr == 'values':
                return "iterate through each value"
                
        return "loop through elements"
    
    def _analyze_while_loop(self, node) -> Optional[str]:
        """Analyze a while loop and describe its purpose."""
        test = node.test
        
        if isinstance(test, ast.Compare):
            # Check for two-pointer pattern: left < right
            if isinstance(test.left, ast.Name) and len(test.comparators) == 1:
                left_name = test.left.id.lower()
                right = test.comparators[0]
                
                if isinstance(right, ast.Name):
                    right_name = right.id.lower()
                    
                    if any(l in left_name for l in ['left', 'lo', 'start', 'i']):
                        if any(r in right_name for r in ['right', 'hi', 'end', 'j']):
                            self.uses_two_pointers = True
                            return "move two pointers toward each other"
                            
        elif isinstance(test, ast.Name):
            name = test.id.lower()
            if name in ['current', 'curr', 'node', 'head']:
                return "traverse the linked list"
            elif name == 'stack':
                return "process elements from stack"
            elif name == 'queue':
                return "process elements from queue"
                
        elif isinstance(test, ast.BoolOp):
            # Check for sliding window pattern
            return "continue while window is valid"
            
        return "continue until condition is met"
    
    def _is_stack_usage(self, node) -> bool:
        """Check if this is a stack-like usage."""
        if isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name):
                var_name = node.func.value.id.lower()
                return 'stack' in var_name
        return False
    
    def _describe_return(self, node) -> Optional[str]:
        """Describe what is being returned."""
        if isinstance(node, ast.Name):
            name = node.id.lower()
            if 'result' in name or 'res' in name or 'ans' in name:
                return "the result"
            return node.id
        elif isinstance(node, ast.List):
            return "a list of results"
        elif isinstance(node, ast.Compare):
            return "a boolean result"
        elif isinstance(node, ast.BinOp):
            return "a computed value"
        elif isinstance(node, ast.Call):
            func = self._get_call_name(node)
            if func == 'join':
                return "the joined string"
            elif func == 'len':
                return "the length"
        return None
    
    def generate_description(self, code: str) -> str:
        """Generate a complete, personalized description of the algorithm."""
        try:
            tree = ast.parse(code)
            self.visit(tree)
            return self._build_description()
        except Exception:
            return "Algorithm implementation."
    
    def _build_description(self) -> str:
        """Build a coherent description from collected information."""
        parts = []
        
        # Special case: string cleaning + reverse = palindrome check
        if self.uses_string_clean and self.uses_reverse:
            return "Clean the string by removing non-alphanumeric characters, then compare with its reverse."
        
        # Special case: linked list traversal + reverse = palindrome check
        if self.uses_reverse and any('linked list' in str(lp).lower() or 'traverse' in str(lp).lower() for lp in self.loop_patterns):
            return "Traverse the linked list to collect values into an array, then compare with its reverse."
        
        # Special case: just reverse comparison
        if self.uses_reverse and not self.loop_patterns:
            return "Reverse the input and compare with original."
        
        # 1. Mention key data structures first
        ds_mentions = []
        for var, desc in self.data_structures.items():
            if 'hash' in desc or 'Counter' in desc or 'mapping' in desc:
                ds_mentions.append(f"Use a {desc}")
            elif 'stack' in desc:
                ds_mentions.append("Use a stack")
            elif 'deque' in desc:
                ds_mentions.append("Use a queue for BFS")
            elif 'set' in desc:
                ds_mentions.append(f"Use a {desc}")
        
        if ds_mentions:
            parts.append(ds_mentions[0])  # Just the primary one
        
        # 2. Mention sorting if used
        if self.uses_sorting and 'sort' not in str(parts):
            parts.append("Sort the input first")
        
        # 3. Describe the main algorithm pattern
        if self.has_recursion:
            if self.helper_funcs:
                parts.append("Use a recursive helper function to explore all possibilities")
            else:
                parts.append("Recursively process each element")
        elif self.uses_heap:
            parts.append("Use a heap to always get the smallest/largest element")
        elif self._is_sliding_window():
            parts.append("Use sliding window to track a valid subarray")
        elif self.uses_two_pointers:
            parts.append("Use two pointers moving toward each other")
        elif self.uses_binary_search:
            parts.append("Use binary search to find the target position")
        elif self.uses_stack and 'stack' not in str(parts).lower():
            parts.append("Use a stack to match pairs or track state")
        
        # 4. Describe loop patterns (avoiding redundancy)
        if len(self.loop_patterns) >= 2:
            has_forward = any('backwards' not in str(lp) for lp in self.loop_patterns)
            has_backward = any('backwards' in str(lp) for lp in self.loop_patterns)
            
            if has_forward and has_backward:
                parts.append("Make two passes: forward then backward")
            elif not self.has_recursion and not self.uses_two_pointers and not self._is_sliding_window():
                if any('index' in str(lp) for lp in self.loop_patterns):
                    parts.append("Use nested loops to check all pairs")
        elif len(self.loop_patterns) == 1 and not parts:
            # Only add loop description if we don't have a better description
            loop_desc = self.loop_patterns[0]
            parts.append(loop_desc.capitalize())
        
        # 5. Describe key operations
        for op in self.key_operations:
            if op not in str(parts).lower():
                parts.append(op.capitalize())
        
        # Build final description
        if not parts:
            parts.append("Process the input directly")
        
        # Clean up: remove redundant mentions
        seen = set()
        unique_parts = []
        for p in parts:
            p_lower = p.lower()
            # Skip if we already mentioned this concept
            if 'stack' in p_lower and 'stack' in str(seen):
                continue
            if 'two pointer' in p_lower and 'two pointer' in str(seen):
                continue
            seen.add(p_lower)
            unique_parts.append(p)
        
        # Join with periods
        description = ". ".join(p.rstrip('.') for p in unique_parts if p)
        
        if not description.endswith('.'):
            description += "."
            
        return description
    
    def _is_sliding_window(self) -> bool:
        """Detect sliding window pattern."""
        # Has left/right or window variables and a hash map
        has_window_vars = len(self.window_vars) >= 2 or 'window' in str(self.window_vars).lower()
        has_dict = any('dict' in desc or 'hash' in desc for desc in self.data_structures.values())
        has_loop = len(self.loop_patterns) > 0
        
        return has_window_vars and (has_dict or has_loop) and not self.uses_two_pointers


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


def analyze_solution_file(file_path: Path) -> Tuple[str, str, str]:
    """Analyze a single solution file and return complexities and description."""
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
        
        # Generate personalized description
        describer = AlgorithmDescriber()
        description = describer.generate_description(code)
        
        return time, space, description
    except Exception:
        return "O(?)", "O(?)", "Algorithm implementation."


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
            content = re.sub(
                r'TODO:\s*Describe your approach here',
                description,
                content,
                flags=re.IGNORECASE
            )
            
            # Also handle "Algorithm:\nTODO..." pattern
            content = re.sub(
                r'(Algorithm:\s*\n)\s*TODO:.*?(\n)',
                f'\\g<1>{description}\\2',
                content,
                flags=re.IGNORECASE
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
