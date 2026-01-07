#!/usr/bin/env python3
"""
Solution Analyzer

This script analyzes the current repository structure to identify:
1. Problems with multiple solutions
2. Different solution approaches/optimizations
3. Performance improvements over time
"""

import os
import re
from pathlib import Path
from datetime import datetime
import ast


def analyze_solution_file(file_path):
    """Analyze a Python solution file to extract metadata."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract timestamp from filename
        timestamp_match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}\.\d{2}\.\d{2})', file_path.name)
        timestamp = None
        if timestamp_match:
            timestamp_str = timestamp_match.group(1).replace('.', ':')
            try:
                timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
            except:
                pass
        
        # Extract runtime and memory from filename
        runtime_match = re.search(r'runtime (\d+)ms', file_path.name)
        memory_match = re.search(r'memory ([\d.]+)MB', file_path.name)
        
        runtime = int(runtime_match.group(1)) if runtime_match else None
        memory = float(memory_match.group(1)) if memory_match else None
        
        # Analyze code complexity (basic heuristics)
        lines = content.split('\n')
        code_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
        
        # Count different algorithmic patterns
        patterns = {
            'nested_loops': len(re.findall(r'for.*for', content)),
            'recursion': content.count('def ') > 1 or 'return ' in content and ('(' in content.split('return')[1] if 'return' in content else ''),
            'hash_map': 'dict(' in content or '{' in content or 'Counter' in content or 'defaultdict' in content,
            'two_pointers': 'left' in content and 'right' in content,
            'sliding_window': 'window' in content or ('left' in content and 'right' in content and ('while' in content or 'for' in content)),
            'binary_search': 'binary_search' in content or ('mid' in content and ('left' in content or 'right' in content)),
            'dfs': 'dfs' in content or ('def ' in content and 'visited' in content),
            'bfs': 'bfs' in content or 'deque' in content or 'queue' in content,
            'dp': 'dp' in content or 'memo' in content or '@lru_cache' in content,
        }
        
        return {
            'file_path': file_path,
            'timestamp': timestamp,
            'runtime': runtime,
            'memory': memory,
            'code_lines': len(code_lines),
            'patterns': patterns,
            'content_preview': content[:200] + '...' if len(content) > 200 else content
        }
    
    except Exception as e:
        return {
            'file_path': file_path,
            'error': str(e)
        }


def analyze_problem_directory(problem_dir):
    """Analyze all solutions for a single problem."""
    solutions = []
    
    for file in problem_dir.iterdir():
        if file.name.endswith('.py'):
            solution_data = analyze_solution_file(file)
            solutions.append(solution_data)
    
    # Sort solutions by timestamp
    solutions = [s for s in solutions if 'timestamp' in s and s['timestamp']]
    solutions.sort(key=lambda x: x['timestamp'] if x['timestamp'] else datetime.min)
    
    return solutions


def find_optimization_patterns(solutions):
    """Identify optimization patterns across multiple solutions."""
    if len(solutions) < 2:
        return []
    
    patterns = []
    
    # Runtime improvements
    runtimes = [s['runtime'] for s in solutions if s['runtime'] is not None]
    if len(runtimes) >= 2:
        if runtimes[-1] < runtimes[0]:  # Latest is faster
            improvement = ((runtimes[0] - runtimes[-1]) / runtimes[0]) * 100
            patterns.append(f"Runtime improved by {improvement:.1f}% ({runtimes[0]}ms → {runtimes[-1]}ms)")
    
    # Memory improvements
    memories = [s['memory'] for s in solutions if s['memory'] is not None]
    if len(memories) >= 2:
        if memories[-1] < memories[0]:  # Latest uses less memory
            improvement = ((memories[0] - memories[-1]) / memories[0]) * 100
            patterns.append(f"Memory improved by {improvement:.1f}% ({memories[0]}MB → {memories[-1]}MB)")
    
    # Algorithmic evolution
    first_patterns = solutions[0]['patterns']
    last_patterns = solutions[-1]['patterns']
    
    for pattern, last_present in last_patterns.items():
        first_present = first_patterns.get(pattern, False)
        if last_present and not first_present:
            patterns.append(f"Added {pattern.replace('_', ' ')} approach")
        elif first_present and not last_present:
            patterns.append(f"Removed {pattern.replace('_', ' ')} approach")
    
    return patterns


def main():
    """Analyze all problems in the repository."""
    print("🔍 Analyzing LeetCode solutions...")
    
    current_dir = Path('.')
    total_problems = 0
    multi_solution_problems = 0
    solution_stats = {}
    optimization_examples = []
    
    # Process each category directory
    for category_dir in current_dir.iterdir():
        if not category_dir.is_dir() or category_dir.name.startswith('.'):
            continue
            
        if category_dir.name in ['array-string', 'linked-list', 'tree', 'dynamic-programming', 
                                'graph', 'binary-search', 'heap', 'trie', 'backtracking', 
                                'math-bit', 'sliding-window', 'two-pointers']:
            
            for difficulty_dir in category_dir.iterdir():
                if not difficulty_dir.is_dir():
                    continue
                
                for problem_dir in difficulty_dir.iterdir():
                    if not problem_dir.is_dir():
                        continue
                    
                    solutions = analyze_problem_directory(problem_dir)
                    total_problems += 1
                    
                    if len(solutions) > 1:
                        multi_solution_problems += 1
                        solution_count = len(solutions)
                        
                        if solution_count not in solution_stats:
                            solution_stats[solution_count] = 0
                        solution_stats[solution_count] += 1
                        
                        # Analyze optimization patterns
                        patterns = find_optimization_patterns(solutions)
                        if patterns:
                            optimization_examples.append({
                                'problem': problem_dir.name,
                                'category': category_dir.name,
                                'difficulty': difficulty_dir.name,
                                'solution_count': solution_count,
                                'patterns': patterns,
                                'time_span': solutions[-1]['timestamp'] - solutions[0]['timestamp'] if solutions[0]['timestamp'] and solutions[-1]['timestamp'] else None
                            })
                        
                        print(f"📁 {problem_dir.name}: {solution_count} solutions")
                        for pattern in patterns:
                            print(f"    ✨ {pattern}")
    
    # Print summary
    print(f"\n📊 SOLUTION ANALYSIS SUMMARY:")
    print(f"Total problems: {total_problems}")
    print(f"Problems with multiple solutions: {multi_solution_problems} ({(multi_solution_problems/total_problems)*100:.1f}%)")
    
    print(f"\n📈 Multiple Solution Distribution:")
    for count, problems in sorted(solution_stats.items()):
        print(f"  {count} solutions: {problems} problems")
    
    print(f"\n🚀 TOP OPTIMIZATION EXAMPLES:")
    optimization_examples.sort(key=lambda x: len(x['patterns']), reverse=True)
    for i, example in enumerate(optimization_examples[:10]):
        print(f"\n{i+1}. {example['problem']} ({example['category']}/{example['difficulty']})")
        print(f"   Solutions: {example['solution_count']}")
        if example['time_span']:
            print(f"   Time span: {example['time_span'].days} days")
        for pattern in example['patterns']:
            print(f"   • {pattern}")


if __name__ == "__main__":
    main()