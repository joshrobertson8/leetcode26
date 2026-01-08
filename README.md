# 🏆 LeetCode Solutions Repository

A comprehensive collection of LeetCode solutions organized by category and difficulty, with automatic syncing from LeetCode.com.

## 🚀 Quick Start

### Automatic Sync (Recommended)

Simply run the sync script - it automatically extracts cookies from your browser and syncs all your accepted solutions:

```bash
python3 leetcode_sync.py
```

**First time?** The script will automatically:
1. Extract cookies from your browser (Chrome, Firefox, Safari, Edge, Opera, or Brave)
2. Authenticate with LeetCode
3. Download all your accepted solutions
4. Organize them into the correct category/difficulty folders
5. Save cookies for future use (no need to authenticate again)

**Subsequent runs:** Just run `python3 leetcode_sync.py` - fully automatic, zero interaction needed!

### Manual Options

```bash
# Specify a browser
python3 leetcode_sync.py --browser chrome

# Pass cookies directly
python3 leetcode_sync.py --cookies "LEETCODE_SESSION=...; csrftoken=..."

# Limit number of submissions
python3 leetcode_sync.py --max 100

# Force re-download all solutions
python3 leetcode_sync.py --force
```

### Installation

```bash
pip3 install -r requirements.txt
```

## 📁 Repository Structure

Solutions are automatically organized into LeetCode's official categories:

```
├── array/
│   ├── easy/
│   └── medium/
├── string/
│   ├── easy/
│   └── medium/
├── hash-table/
├── linked-list/
├── tree/
├── dynamic-programming/
├── backtracking/
├── graph/
├── binary-search/
├── heap/
├── trie/
├── stack/
├── sliding-window/
├── two-pointers/
├── bit-manipulation/
├── math/
├── greedy/
├── sorting/
└── design/
```

Each problem follows this structure:
```
category/difficulty/problem-name/
├── problem-name.txt                    # Problem statement
├── YYYY-MM-DD HH.MM.SS - Solution1.py # Timestamped solutions
└── YYYY-MM-DD HH.MM.SS - Solution2.py # Multiple solutions preserved
```

## 🎯 Features

- ✅ **Fully automatic syncing** - No manual setup needed
- ✅ **Multiple solutions preserved** - All versions of your solutions are kept
- ✅ **Automatic organization** - Solutions sorted by category and difficulty
- ✅ **Problem statements** - Automatically downloads problem descriptions
- ✅ **Performance tracking** - Runtime and memory usage in filenames
- ✅ **Duplicate prevention** - Skips existing solutions automatically

## 📊 Statistics

- **Total Problems**: 150+
- **Total Solutions**: 300+ (multiple solutions per problem)
- **Categories**: 18 official LeetCode categories
- **Difficulties**: Easy, Medium, Hard

## 🔧 How It Works

1. **Authentication**: Extracts LeetCode session cookies from your browser automatically
2. **Fetching**: Uses LeetCode's GraphQL API to get all accepted submissions
3. **Organization**: Categorizes problems using LeetCode's topic tags and problem metadata
4. **Storage**: Saves solutions with timestamps, runtime, and memory metrics

## 📝 Notes

- Cookies are saved to `.leetcode_config.json` (gitignored for security)
- Solutions are organized exactly as they appear on LeetCode
- Multiple solutions for the same problem are all preserved
- Problem statements are converted from HTML to plain text

## 🛠 Troubleshooting

**Can't extract cookies?**
- Make sure you're logged into LeetCode in at least one browser
- Try specifying a browser: `--browser chrome`
- Or use manual setup: `--setup`

**Authentication failed?**
- Cookies may have expired - run `--setup` to update them
- Or pass cookies directly with `--cookies`

**Missing solutions?**
- Use `--force` to re-download everything
- Increase `--max` to fetch more submissions

---

*Automatically synced from LeetCode.com - Just run `python3 leetcode_sync.py`!*
