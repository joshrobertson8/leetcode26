#!/usr/bin/env python3
"""
LeetCode Solution Syncer

Automatically syncs your LeetCode accepted solutions to your local repository.
Supports multiple authentication methods and organizes solutions by category/difficulty.

Usage:
    python leetcode_sync.py              # Automatic mode - tries browser extraction, then prompts if needed
    python leetcode_sync.py --browser chrome  # Extract cookies from specific browser
    python leetcode_sync.py --cookies "..."   # Pass cookies directly (best for long strings)
    python leetcode_sync.py --setup          # Interactive setup with cookie configuration
"""

import os
import re
import sys
import json
import time
import hashlib
import argparse
import requests
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from urllib.parse import urljoin

# ==============================================================================
# CLI Output System - Clean Professional Design
# ==============================================================================

class CLI:
    """Professional CLI output with tables and clean formatting."""
    
    WIDTH = 72
    
    # Box drawing characters
    BOX_H = "-"
    BOX_V = "|"
    BOX_TL = "+"
    BOX_TR = "+"
    BOX_BL = "+"
    BOX_BR = "+"
    BOX_ML = "+"
    BOX_MR = "+"
    BOX_TM = "+"
    BOX_BM = "+"
    BOX_CROSS = "+"
    
    @classmethod
    def header(cls, title: str):
        """Print a boxed header."""
        line = cls.BOX_H * (cls.WIDTH - 2)
        print(f"\n{cls.BOX_TL}{line}{cls.BOX_TR}")
        padding = cls.WIDTH - 4 - len(title)
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"{cls.BOX_V} {' ' * left_pad}{title}{' ' * right_pad} {cls.BOX_V}")
        print(f"{cls.BOX_BL}{line}{cls.BOX_BR}")
    
    @classmethod
    def section(cls, title: str):
        """Print a section divider."""
        print(f"\n{'─' * 40}")
        print(f"  {title}")
        print(f"{'─' * 40}")
    
    @classmethod
    def status(cls, label: str, value: str, status: str = "info"):
        """Print a status line with label and value."""
        symbols = {"ok": "[+]", "error": "[!]", "warn": "[*]", "info": "   "}
        sym = symbols.get(status, "   ")
        print(f"{sym} {label}: {value}")
    
    @classmethod
    def log(cls, message: str, status: str = "info"):
        """Print a log message."""
        symbols = {"ok": "[+]", "error": "[!]", "warn": "[*]", "info": "   ", "save": " > "}
        sym = symbols.get(status, "   ")
        print(f"{sym} {message}")
    
    @classmethod
    def progress(cls, current: int, total: int, prefix: str = "Progress"):
        """Print a progress indicator."""
        pct = (current / total * 100) if total > 0 else 0
        bar_width = 30
        filled = int(bar_width * current / total) if total > 0 else 0
        bar = "=" * filled + "-" * (bar_width - filled)
        print(f"\r    {prefix}: [{bar}] {current}/{total} ({pct:.0f}%)", end="", flush=True)
    
    @classmethod
    def progress_done(cls):
        """Complete the progress line."""
        print()
    
    @classmethod
    def table_start(cls, columns: List[Tuple[str, int]]):
        """Start a table with column headers."""
        # Build header line
        header_parts = []
        sep_parts = []
        for name, width in columns:
            header_parts.append(f" {name:<{width}} ")
            sep_parts.append(cls.BOX_H * (width + 2))
        
        print(f"{cls.BOX_TL}{cls.BOX_TM.join(sep_parts)}{cls.BOX_TR}")
        print(f"{cls.BOX_V}{cls.BOX_V.join(header_parts)}{cls.BOX_V}")
        print(f"{cls.BOX_ML}{cls.BOX_CROSS.join(sep_parts)}{cls.BOX_MR}")
    
    @classmethod
    def table_row(cls, values: List[str], widths: List[int]):
        """Print a table row."""
        parts = []
        for val, width in zip(values, widths):
            # Truncate if too long
            if len(val) > width:
                val = val[:width-2] + ".."
            parts.append(f" {val:<{width}} ")
        print(f"{cls.BOX_V}{cls.BOX_V.join(parts)}{cls.BOX_V}")
    
    @classmethod
    def table_end(cls, widths: List[int]):
        """End a table."""
        sep_parts = [cls.BOX_H * (w + 2) for w in widths]
        print(f"{cls.BOX_BL}{cls.BOX_BM.join(sep_parts)}{cls.BOX_BR}")
    
    @classmethod
    def summary_box(cls, stats: Dict[str, any]):
        """Print a summary statistics box."""
        print()
        line = cls.BOX_H * (cls.WIDTH - 2)
        print(f"{cls.BOX_TL}{line}{cls.BOX_TR}")
        
        title = "SYNC SUMMARY"
        padding = cls.WIDTH - 4 - len(title)
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"{cls.BOX_V} {' ' * left_pad}{title}{' ' * right_pad} {cls.BOX_V}")
        print(f"{cls.BOX_ML}{line}{cls.BOX_MR}")
        
        for key, value in stats.items():
            text = f"{key}: {value}"
            padding = cls.WIDTH - 4 - len(text)
            print(f"{cls.BOX_V}  {text}{' ' * padding} {cls.BOX_V}")
        
        print(f"{cls.BOX_BL}{line}{cls.BOX_BR}")
    
    @classmethod
    def blank(cls):
        """Print a blank line."""
        print()


# ==============================================================================
# Configuration
# ==============================================================================

BASE_DIR = Path(__file__).parent
CONFIG_FILE = BASE_DIR / ".leetcode_config.json"
LEETCODE_BASE_URL = "https://leetcode.com"
LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"

# Request headers to mimic browser
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json",
    "Origin": "https://leetcode.com",
    "Referer": "https://leetcode.com",
}

# ==============================================================================
# Data Models
# ==============================================================================

@dataclass
class Submission:
    id: str
    title: str
    title_slug: str
    timestamp: int
    status_display: str
    runtime: str
    memory: str
    lang: str
    code: str = ""
    problem_id: str = ""
    difficulty: str = ""
    category: str = ""


@dataclass
class Problem:
    id: str
    title: str
    title_slug: str
    difficulty: str
    content: str
    category_slugs: List[str]


# ==============================================================================
# LeetCode API Client
# ==============================================================================

class LeetCodeClient:
    """Client for interacting with LeetCode's GraphQL API."""
    
    def __init__(self, session_cookie: str, csrf_token: str = ""):
        self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)
        
        # Set cookies
        self.session.cookies.set("LEETCODE_SESSION", session_cookie, domain="leetcode.com")
        if csrf_token:
            self.session.cookies.set("csrftoken", csrf_token, domain="leetcode.com")
            self.session.headers["x-csrftoken"] = csrf_token
    
    def _graphql_request(self, query: str, variables: dict = None) -> dict:
        """Make a GraphQL request to LeetCode."""
        payload = {"query": query}
        if variables:
            payload["variables"] = variables
        
        response = self.session.post(LEETCODE_GRAPHQL_URL, json=payload)
        response.raise_for_status()
        
        data = response.json()
        if "errors" in data:
            raise Exception(f"GraphQL error: {data['errors']}")
        
        return data.get("data", {})
    
    def get_user_profile(self) -> Optional[dict]:
        """Get current user's profile to verify authentication."""
        query = """
        query globalData {
            userStatus {
                userId
                username
                isSignedIn
                isPremium
            }
        }
        """
        try:
            data = self._graphql_request(query)
            return data.get("userStatus")
        except Exception as e:
            CLI.log(f"Authentication check failed: {e}", "error")
            return None
    
    def get_submissions_list(self, offset: int = 0, limit: int = 20, last_key: str = None) -> Tuple[List[dict], str, bool]:
        """Get list of user's submissions."""
        query = """
        query submissionList($offset: Int!, $limit: Int!, $lastKey: String) {
            submissionList(offset: $offset, limit: $limit, lastKey: $lastKey) {
                lastKey
                hasNext
                submissions {
                    id
                    statusDisplay
                    lang
                    runtime
                    timestamp
                    url
                    isPending
                    memory
                    title
                    titleSlug
                }
            }
        }
        """
        variables = {
            "offset": offset,
            "limit": limit,
        }
        if last_key:
            variables["lastKey"] = last_key
        
        data = self._graphql_request(query, variables)
        submission_list = data.get("submissionList", {})
        submissions = submission_list.get("submissions", [])
        last_key = submission_list.get("lastKey")
        has_next = submission_list.get("hasNext", False)
        
        # Filter to only accepted submissions
        accepted = [s for s in submissions if s.get("statusDisplay") == "Accepted"]
        
        return accepted, last_key, has_next
    
    def get_all_accepted_submissions(self, max_submissions: int = 1000) -> List[dict]:
        """Fetch all accepted submissions with pagination."""
        all_submissions = []
        offset = 0
        limit = 20
        last_key = None
        
        CLI.log("Fetching accepted submissions from LeetCode...")
        
        while len(all_submissions) < max_submissions:
            submissions, last_key, has_next = self.get_submissions_list(
                offset=offset, limit=limit, last_key=last_key
            )
            
            if not submissions:
                break
            
            all_submissions.extend(submissions)
            CLI.progress(len(all_submissions), max_submissions, "Fetching")
            
            if not has_next:
                break
            
            offset += limit
            time.sleep(0.5)  # Rate limiting
        
        CLI.progress_done()
        return all_submissions[:max_submissions]
    
    def get_submission_detail(self, submission_id: str) -> Optional[dict]:
        """Get detailed submission including code."""
        query = """
        query submissionDetails($submissionId: Int!) {
            submissionDetails(submissionId: $submissionId) {
                runtime
                runtimeDisplay
                runtimePercentile
                runtimeDistribution
                memory
                memoryDisplay
                memoryPercentile
                memoryDistribution
                code
                timestamp
                statusCode
                lang {
                    name
                    verboseName
                }
                question {
                    questionId
                    titleSlug
                    title
                    difficulty
                    topicTags {
                        name
                        slug
                    }
                    content
                }
            }
        }
        """
        variables = {"submissionId": int(submission_id)}
        
        try:
            data = self._graphql_request(query, variables)
            return data.get("submissionDetails")
        except Exception:
            return None
    
    def get_problem_detail(self, title_slug: str) -> Optional[dict]:
        """Get problem details."""
        query = """
        query questionData($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                questionFrontendId
                title
                titleSlug
                difficulty
                content
                topicTags {
                    name
                    slug
                }
            }
        }
        """
        variables = {"titleSlug": title_slug}
        
        try:
            data = self._graphql_request(query, variables)
            return data.get("question")
        except Exception:
            return None


# ==============================================================================
# Browser Cookie Extraction
# ==============================================================================

def extract_cookies_from_browser(browser: str = None) -> Tuple[str, str]:
    """
    Extract LeetCode cookies from browser automatically.
    Tries multiple browsers if browser is not specified.
    Requires browser_cookie3 library.
    """
    try:
        import browser_cookie3  # type: ignore
    except ImportError:
        CLI.log("browser_cookie3 not installed", "error")
        CLI.log("Install with: pip install browser_cookie3")
        return "", ""
    
    browsers_to_try = []
    
    if browser:
        browsers_to_try = [browser.lower()]
    else:
        # Try browsers in order of popularity
        browsers_to_try = ["chrome", "firefox", "safari", "edge", "opera", "brave"]
    
    for browser_name in browsers_to_try:
        try:
            CLI.log(f"Checking {browser_name}...")
            
            if browser_name == "chrome":
                cj = browser_cookie3.chrome(domain_name=".leetcode.com")
            elif browser_name == "firefox":
                cj = browser_cookie3.firefox(domain_name=".leetcode.com")
            elif browser_name == "safari":
                cj = browser_cookie3.safari(domain_name=".leetcode.com")
            elif browser_name == "edge":
                cj = browser_cookie3.edge(domain_name=".leetcode.com")
            elif browser_name == "opera":
                cj = browser_cookie3.opera(domain_name=".leetcode.com")
            elif browser_name == "brave":
                cj = browser_cookie3.brave(domain_name=".leetcode.com")
            else:
                continue
            
            session_cookie = ""
            csrf_token = ""
            
            for cookie in cj:
                if cookie.name == "LEETCODE_SESSION":
                    session_cookie = cookie.value
                elif cookie.name == "csrftoken":
                    csrf_token = cookie.value
            
            if session_cookie:
                CLI.log(f"Found cookies in {browser_name}", "ok")
                return session_cookie, csrf_token
            else:
                CLI.log(f"No LeetCode session in {browser_name}", "warn")
        
        except browser_cookie3.BrowserCookieError:
            CLI.log(f"{browser_name} not available", "warn")
            continue
        except Exception:
            continue
    
    CLI.log("Could not extract cookies from any browser", "error")
    return "", ""


# ==============================================================================
# Problem Categorization (matching existing structure)
# ==============================================================================

def categorize_problem(title: str, topic_tags: List[str]) -> str:
    """
    Categorize problem using existing repository structure.
    """
    title_lower = title.lower()
    tag_slugs = [tag.lower() for tag in topic_tags]
    
    # Priority-based category mapping
    category_mappings = [
        ("trie", ["trie", "prefix-tree"]),
        ("design", ["design"]),
        ("heap", ["heap", "priority-queue", "heap-priority-queue"]),
        ("graph", ["graph", "depth-first-search", "breadth-first-search"]),
        ("tree", ["tree", "binary-tree", "binary-search-tree"]),
        ("linked-list", ["linked-list"]),
        ("stack", ["stack", "monotonic-stack"]),
        ("sliding-window", ["sliding-window"]),
        ("two-pointers", ["two-pointers"]),
        ("binary-search", ["binary-search"]),
        ("backtracking", ["backtracking"]),
        ("dynamic-programming", ["dynamic-programming"]),
        ("greedy", ["greedy"]),
        ("bit-manipulation", ["bit-manipulation"]),
        ("sorting", ["sorting", "merge-sort", "quick-sort", "bucket-sort"]),
        ("math", ["math", "number-theory"]),
        ("hash-table", ["hash-table"]),
        ("string", ["string"]),
        ("array", ["array"]),
    ]
    
    for category, tags in category_mappings:
        for tag in tags:
            if tag in tag_slugs:
                return category
    
    # Title-based fallback
    title_patterns = {
        "string": ["palindrome", "anagram", "substring", "string", "word", "roman"],
        "array": ["array", "sum", "subarray", "merge", "sort", "remove", "duplicate"],
        "linked-list": ["linked list", "list node"],
        "tree": ["tree", "binary tree", "depth", "height", "traversal"],
        "hash-table": ["hash", "contains duplicate", "two sum"],
        "dynamic-programming": ["climbing", "house robber", "coin change"],
        "bit-manipulation": ["bit", "single number", "power of two"],
        "math": ["power of", "happy number", "perfect square"],
        "stack": ["parentheses", "brackets", "valid parentheses"],
    }
    
    for category, patterns in title_patterns.items():
        for pattern in patterns:
            if pattern in title_lower:
                return category
    
    return "array"


def html_to_text(html_content: str) -> str:
    """Convert HTML content to plain text."""
    if not html_content:
        return ""
    
    try:
        import html2text
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_images = True
        h.body_width = 0
        text = h.handle(html_content)
        
        text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
        text = re.sub(r'\*(.*?)\*', r'\1', text)
        text = re.sub(r'`(.*?)`', r'\1', text)
        text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)
        
        return text.strip()
    except ImportError:
        text = re.sub(r'<[^>]+>', '', html_content)
        text = re.sub(r'&nbsp;', ' ', text)
        text = re.sub(r'&lt;', '<', text)
        text = re.sub(r'&gt;', '>', text)
        text = re.sub(r'&amp;', '&', text)
        return text.strip()


# ==============================================================================
# Solution Organization
# ==============================================================================

class SolutionOrganizer:
    """Organizes solutions into the existing repository structure."""
    
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
    
    def get_existing_solutions(self) -> Dict[str, List[str]]:
        """Scan existing solutions and return mapping of problem_slug -> existing files."""
        existing = {}
        
        for category_dir in self.base_dir.iterdir():
            if not category_dir.is_dir() or category_dir.name.startswith('.'):
                continue
            
            for difficulty_dir in category_dir.iterdir():
                if not difficulty_dir.is_dir():
                    continue
                
                for problem_dir in difficulty_dir.iterdir():
                    if not problem_dir.is_dir():
                        continue
                    
                    problem_name = problem_dir.name
                    py_files = [f.name for f in problem_dir.glob("*.py")]
                    
                    if py_files:
                        existing[problem_name] = py_files
        
        return existing
    
    def solution_exists(self, problem_slug: str, timestamp: int, existing: Dict[str, List[str]]) -> bool:
        """Check if a solution already exists based on timestamp."""
        problem_dir_name = None
        for dir_name in existing.keys():
            if problem_slug in dir_name or dir_name.endswith(f"-{problem_slug}"):
                problem_dir_name = dir_name
                break
        
        if not problem_dir_name:
            return False
        
        try:
            timestamp_int = int(timestamp) if isinstance(timestamp, str) else timestamp
            dt = datetime.fromtimestamp(timestamp_int)
        except (ValueError, TypeError, OSError):
            return False
        date_str = dt.strftime("%Y-%m-%d %H.%M.%S")
        
        for filename in existing.get(problem_dir_name, []):
            if date_str in filename:
                return True
        
        return False
    
    def save_solution(self, submission: dict, problem: dict) -> Tuple[bool, str]:
        """Save a solution to the repository. Returns (saved, file_path)"""
        title_slug = submission.get("titleSlug") or problem.get("titleSlug", "")
        question_id = problem.get("questionFrontendId") or problem.get("questionId", "0")
        title = problem.get("title", title_slug)
        difficulty = problem.get("difficulty", "Medium").lower()
        
        topic_tags = [tag["slug"] for tag in problem.get("topicTags", [])]
        category = categorize_problem(title, topic_tags)
        
        clean_title = re.sub(r'[^\w\s-]', '', title.lower())
        clean_title = re.sub(r'[\s]+', '-', clean_title)
        dir_name = f"{question_id}-{clean_title}"
        
        problem_dir = self.base_dir / category / difficulty / dir_name
        problem_dir.mkdir(parents=True, exist_ok=True)
        
        # Save problem statement
        txt_file = problem_dir / f"{dir_name}.txt"
        if not txt_file.exists() and problem.get("content"):
            content = problem["content"]
            plain_text = html_to_text(content)
            header = f"# {question_id} - {title}\n\n## Difficulty: {difficulty.capitalize()}\n\n"
            full_text = header + plain_text
            txt_file.write_text(full_text, encoding="utf-8")
        
        # Create solution filename
        timestamp = submission.get("timestamp", int(time.time()))
        try:
            timestamp_int = int(timestamp) if isinstance(timestamp, str) else timestamp
            dt = datetime.fromtimestamp(timestamp_int)
        except (ValueError, TypeError, OSError):
            dt = datetime.now()
        date_str = dt.strftime("%Y-%m-%d %H.%M.%S")
        
        runtime = submission.get("runtimeDisplay", submission.get("runtime", "0ms"))
        if not runtime.endswith("ms"):
            runtime = f"{runtime}ms"
        runtime = runtime.replace(" ", "")
        
        memory = submission.get("memoryDisplay", submission.get("memory", "0MB"))
        if not memory.endswith("MB"):
            memory = f"{memory}MB"
        memory = memory.replace(" ", "")
        
        filename = f"{date_str} - Accepted - runtime {runtime} - memory {memory}.py"
        solution_file = problem_dir / filename
        
        if solution_file.exists():
            return False, str(solution_file)
        
        code = submission.get("code", "")
        if not code:
            return False, ""
        
        header_comment = f'''"""
LeetCode: {dt.strftime("%Y %m %d %H.%M.%S")} Accepted Runtime {runtime} Memory {memory}

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

'''
        if not code.strip().startswith('"""') and not code.strip().startswith("'''"):
            code = header_comment + code
        
        solution_file.write_text(code, encoding="utf-8")
        
        # Automatically analyze and update complexity and description
        try:
            # Import here to avoid circular dependencies
            import sys
            import importlib.util
            analyzer_path = BASE_DIR / "analyze_complexity.py"
            if analyzer_path.exists():
                spec = importlib.util.spec_from_file_location("analyze_complexity", analyzer_path)
                analyzer_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(analyzer_module)
                
                time_comp, space_comp, description = analyzer_module.analyze_solution_file(solution_file)
                if time_comp != "O(?)" or space_comp != "O(?)":
                    analyzer_module.update_solution_file(solution_file, time_comp, space_comp, description)
        except Exception:
            pass  # Don't fail if complexity analysis fails
        
        return True, str(solution_file)


# ==============================================================================
# Configuration Management
# ==============================================================================

def load_config() -> dict:
    """Load configuration from file."""
    if CONFIG_FILE.exists():
        try:
            return json.loads(CONFIG_FILE.read_text())
        except:
            pass
    return {}


def save_config(config: dict):
    """Save configuration to file."""
    CONFIG_FILE.write_text(json.dumps(config, indent=2))
    CLI.log("Configuration saved", "ok")


def parse_cookie_string(cookie_string: str) -> Tuple[str, str]:
    """Parse a cookie string and extract LEETCODE_SESSION and csrftoken."""
    session_cookie = ""
    csrf_token = ""
    
    cookies = re.split(r';\s*', cookie_string.strip())
    
    for cookie in cookies:
        cookie = cookie.strip()
        if not cookie:
            continue
        
        if '=' in cookie:
            key, value = cookie.split('=', 1)
            key = key.strip()
            value = value.strip()
            
            if key == "LEETCODE_SESSION":
                session_cookie = value
            elif key == "csrftoken":
                csrf_token = value
    
    return session_cookie, csrf_token


def setup_interactive() -> Tuple[str, str]:
    """Interactive setup for LeetCode credentials."""
    CLI.header("LeetCode Authentication Setup")
    print("""
  To sync your LeetCode solutions, provide your session cookies.

  How to get your cookies:
  1. Open LeetCode.com in your browser and log in
  2. Open Developer Tools (F12 or Cmd+Option+I)
  3. Go to Application/Storage > Cookies > leetcode.com
  4. Copy the LEETCODE_SESSION and csrftoken values

  You can paste the full cookie string - it will be parsed automatically.
""")
    
    print("  Paste your cookie string (Enter twice when done):")
    
    lines = []
    try:
        while True:
            line = input()
            if line.strip() == "" and lines:
                break
            lines.append(line)
    except EOFError:
        pass
    
    cookie_string = " ".join(lines).strip()
    
    if not cookie_string:
        session_cookie = input("  LEETCODE_SESSION: ").strip()
        csrf_token = input("  csrftoken (optional): ").strip()
        return session_cookie, csrf_token
    
    session_cookie, csrf_token = parse_cookie_string(cookie_string)
    
    if not session_cookie:
        CLI.log("Could not find LEETCODE_SESSION in input", "warn")
        session_cookie = input("  LEETCODE_SESSION: ").strip()
        if not csrf_token:
            csrf_token = input("  csrftoken (optional): ").strip()
    
    return session_cookie, csrf_token


# ==============================================================================
# Main Sync Logic
# ==============================================================================

def sync_solutions(client: LeetCodeClient, organizer: SolutionOrganizer, 
                   max_submissions: int = 500, force: bool = False):
    """Main sync function."""
    
    CLI.section("Scanning Repository")
    existing = organizer.get_existing_solutions()
    CLI.status("Existing problems", str(len(existing)))
    
    # Fetch submissions
    CLI.section("Fetching Submissions")
    submissions = client.get_all_accepted_submissions(max_submissions)
    CLI.status("Total accepted", str(len(submissions)))
    
    if not submissions:
        CLI.log("No submissions to sync")
        return
    
    # Process unique problems
    unique_problems: Dict[str, dict] = {}
    for sub in submissions:
        slug = sub.get("titleSlug", "")
        if slug and (slug not in unique_problems or 
                     sub.get("timestamp", 0) > unique_problems[slug].get("timestamp", 0)):
            unique_problems[slug] = sub
    
    CLI.status("Unique problems", str(len(unique_problems)))
    
    # Track submissions per problem
    problem_submissions: Dict[str, List[dict]] = {}
    for sub in submissions:
        slug = sub.get("titleSlug", "")
        if slug:
            if slug not in problem_submissions:
                problem_submissions[slug] = []
            problem_submissions[slug].append(sub)
    
    # Sync
    CLI.section("Syncing Solutions")
    
    new_count = 0
    updated_count = 0
    skipped_count = 0
    failed_count = 0
    saved_files = []
    
    total_problems = len(problem_submissions)
    current = 0
    
    # Load analyzer module once
    analyzer_module = None
    try:
        import sys
        import importlib.util
        analyzer_path = BASE_DIR / "analyze_complexity.py"
        if analyzer_path.exists():
            spec = importlib.util.spec_from_file_location("analyze_complexity", analyzer_path)
            analyzer_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(analyzer_module)
    except Exception:
        pass
    
    for slug, subs in problem_submissions.items():
        current += 1
        subs.sort(key=lambda x: x.get("timestamp", 0), reverse=True)
        
        problem = client.get_problem_detail(slug)
        if not problem:
            failed_count += len(subs)
            continue
        
        for sub in subs:
            timestamp = sub.get("timestamp", 0)
            
            # Always fetch submission details for analysis
            sub_detail = client.get_submission_detail(sub.get("id", ""))
            if not sub_detail:
                failed_count += 1
                continue
            
            full_sub = {**sub, **sub_detail}
            
            # Check if solution exists
            solution_exists = organizer.solution_exists(slug, timestamp, existing)
            
            if not force and solution_exists:
                # Update existing file with complexity and description
                updated = False
                try:
                    # Find the existing file
                    problem_dir_name = None
                    for dir_name in existing.keys():
                        if slug in dir_name or dir_name.endswith(f"-{slug}"):
                            problem_dir_name = dir_name
                            break
                    
                    if problem_dir_name and analyzer_module:
                        try:
                            timestamp_int = int(timestamp) if isinstance(timestamp, str) else timestamp
                            dt = datetime.fromtimestamp(timestamp_int)
                            date_str = dt.strftime("%Y-%m-%d %H.%M.%S")
                            
                            # Find the matching file
                            for category_dir in BASE_DIR.iterdir():
                                if not category_dir.is_dir() or category_dir.name.startswith('.'):
                                    continue
                                for difficulty_dir in category_dir.iterdir():
                                    if not difficulty_dir.is_dir():
                                        continue
                                    for prob_dir in difficulty_dir.iterdir():
                                        if prob_dir.name == problem_dir_name:
                                            for py_file in prob_dir.glob("*.py"):
                                                if date_str in py_file.name:
                                                    # Update this file
                                                    time_comp, space_comp, description = analyzer_module.analyze_solution_file(py_file)
                                                    if time_comp != "O(?)" or space_comp != "O(?)":
                                                        analyzer_module.update_solution_file(py_file, time_comp, space_comp, description)
                                                        updated = True
                                                    break
                        except Exception:
                            pass
                except Exception:
                    pass
                
                if updated:
                    updated_count += 1
                else:
                    skipped_count += 1
                continue
            
            # Save new solution
            saved, filepath = organizer.save_solution(full_sub, problem)
            
            if saved:
                new_count += 1
                saved_files.append((slug, Path(filepath).name))
            else:
                if filepath:
                    skipped_count += 1
                else:
                    failed_count += 1
            
            time.sleep(0.3)
        
        CLI.progress(current, total_problems, "Problems")
        time.sleep(0.2)
    
    CLI.progress_done()
    
    # Show saved files
    if saved_files:
        CLI.section("New Solutions Saved")
        
        # Group by problem
        col_widths = [35, 30]
        CLI.table_start([("Problem", col_widths[0]), ("File", col_widths[1])])
        
        for problem, filename in saved_files[:20]:  # Show first 20
            CLI.table_row([problem, filename], col_widths)
        
        if len(saved_files) > 20:
            CLI.table_row([f"... and {len(saved_files) - 20} more", ""], col_widths)
        
        CLI.table_end(col_widths)
    
    # Summary
    CLI.summary_box({
        "New solutions saved": new_count,
        "Existing solutions updated": updated_count,
        "Already up to date": skipped_count,
        "Failed": failed_count,
        "Total processed": new_count + updated_count + skipped_count + failed_count
    })


# ==============================================================================
# CLI Entry Point
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Sync LeetCode solutions to your local repository",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python leetcode_sync.py              # Auto-sync using saved credentials
  python leetcode_sync.py --setup      # Interactive setup
  python leetcode_sync.py --browser chrome  # Extract from browser
  python leetcode_sync.py --max 100    # Limit to 100 submissions
        """
    )
    parser.add_argument("--setup", action="store_true", help="Run interactive setup")
    parser.add_argument("--browser", type=str, choices=["chrome", "firefox", "safari", "edge", "opera", "brave"])
    parser.add_argument("--cookies", type=str, help="Pass cookie string directly")
    parser.add_argument("--cookie-file", type=str, help="Read cookies from file")
    parser.add_argument("--max", type=int, default=500, help="Max submissions to fetch")
    parser.add_argument("--force", action="store_true", help="Force re-download")
    
    args = parser.parse_args()
    
    CLI.header("LeetCode Solution Syncer")
    
    config = load_config()
    session_cookie = config.get("session_cookie", "")
    csrf_token = config.get("csrf_token", "")
    
    # Handle credentials
    if args.setup:
        session_cookie, csrf_token = setup_interactive()
        if session_cookie:
            save_config({"session_cookie": session_cookie, "csrf_token": csrf_token})
    
    elif args.cookies:
        CLI.log("Parsing cookies from command line...")
        session_cookie, csrf_token = parse_cookie_string(args.cookies)
        if session_cookie:
            CLI.log("Cookies parsed successfully", "ok")
            save_config({"session_cookie": session_cookie, "csrf_token": csrf_token})
        else:
            CLI.log("Could not find LEETCODE_SESSION", "error")
            sys.exit(1)
    
    elif args.cookie_file:
        cookie_file_path = Path(args.cookie_file)
        if not cookie_file_path.exists():
            CLI.log(f"Cookie file not found: {cookie_file_path}", "error")
            sys.exit(1)
        
        CLI.log(f"Reading cookies from {cookie_file_path}...")
        cookie_string = cookie_file_path.read_text(encoding="utf-8").strip()
        session_cookie, csrf_token = parse_cookie_string(cookie_string)
        if session_cookie:
            CLI.log("Cookies parsed successfully", "ok")
            save_config({"session_cookie": session_cookie, "csrf_token": csrf_token})
        else:
            CLI.log("Could not find LEETCODE_SESSION", "error")
            sys.exit(1)
    
    elif args.browser:
        CLI.log(f"Extracting cookies from {args.browser}...")
        session_cookie, csrf_token = extract_cookies_from_browser(args.browser)
        if session_cookie:
            save_config({"session_cookie": session_cookie, "csrf_token": csrf_token})
        else:
            CLI.log("Trying other browsers...", "warn")
            session_cookie, csrf_token = extract_cookies_from_browser()
            if session_cookie:
                save_config({"session_cookie": session_cookie, "csrf_token": csrf_token})
            else:
                CLI.log("Could not extract cookies", "error")
                sys.exit(1)
    
    elif not session_cookie:
        CLI.log("No credentials found. Attempting browser extraction...", "warn")
        session_cookie, csrf_token = extract_cookies_from_browser()
        
        if session_cookie:
            CLI.log("Cookies extracted successfully", "ok")
            save_config({"session_cookie": session_cookie, "csrf_token": csrf_token})
        else:
            CLI.log("Browser extraction failed", "warn")
            CLI.log("Use --setup for manual entry or --cookies to pass directly")
            session_cookie, csrf_token = setup_interactive()
            if session_cookie:
                save_config({"session_cookie": session_cookie, "csrf_token": csrf_token})
    
    if not session_cookie:
        CLI.log("No session cookie provided", "error")
        sys.exit(1)
    
    # Verify auth
    CLI.section("Authentication")
    client = LeetCodeClient(session_cookie, csrf_token)
    
    user = client.get_user_profile()
    if not user or not user.get("isSignedIn"):
        CLI.log("Authentication failed - cookie may be expired", "error")
        CLI.log("Run: python leetcode_sync.py --setup")
        sys.exit(1)
    
    CLI.status("User", user.get('username', 'Unknown'), "ok")
    if user.get("isPremium"):
        CLI.status("Account", "Premium", "ok")
    
    # Run sync
    organizer = SolutionOrganizer(BASE_DIR)
    sync_solutions(client, organizer, max_submissions=args.max, force=args.force)
    
    CLI.blank()
    CLI.log("Sync complete", "ok")


if __name__ == "__main__":
    main()
