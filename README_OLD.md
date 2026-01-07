# LeetCode Solutions Export

This repository contains all accepted LeetCode solutions exported using `leetcode-export`.

## 🚀 Quick Start Guide

### Step 1: Get LeetCode Authentication Cookies

1. Open [leetcode.com](https://leetcode.com) and log in
2. Open DevTools (Cmd + Option + I on macOS)
3. Go to the **Network** tab
4. Refresh the page (Cmd + R)
5. Click any request to `leetcode.com` in the network requests list
6. Find the **Cookie** header in the request headers
7. Copy the entire cookie string (it will be very long)

**Example cookie format:**

```
LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...; csrftoken=abcd1234...; cf_clearance=xyz789...
```

### Step 2: Export Your Solutions

Choose one of the export options below:

#### Option A: Basic Export (All in one folder)

```bash
./export_basic.sh
```

#### Option B: Topic Grouped Export (Organized by algorithm topics)

```bash
./export_grouped.sh
```

Both scripts will prompt you to paste your cookie string.

### Step 3: Format Solutions (Optional)

```bash
python format_solutions.py
```

This adds consistent headers with placeholders for time/space complexity analysis.

### Step 4: Commit to Git

```bash
git add .
git commit -m "Import accepted LeetCode solutions via leetcode-export"
```

## 📁 Repository Structure

After export, you'll have:

### Basic Export:

```
.
├── two-sum.py
├── add-two-numbers.py
├── longest-substring-without-repeating-characters.py
└── ...
```

### Topic-Grouped Export:

```
.
├── arrays/
│   ├── two-sum.py
│   ├── best-time-to-buy-and-sell-stock.py
│   └── ...
├── dynamic-programming/
│   ├── climbing-stairs.py
│   ├── house-robber.py
│   └── ...
├── graphs/
│   ├── number-of-islands.py
│   └── ...
└── ...
```

## 🔧 Manual Export Commands

If you prefer to run the export manually:

### Basic Export

```bash
/Users/joshrobertson8/projects/leetcode26/.venv/bin/python -m leetcode_export \
  --cookies "YOUR_COOKIE_STRING_HERE" \
  --only-accepted \
  --language python \
  --folder .
```

### Topic-Grouped Export

```bash
/Users/joshrobertson8/projects/leetcode26/.venv/bin/python -m leetcode_export \
  --cookies "YOUR_COOKIE_STRING_HERE" \
  --only-accepted \
  --language python \
  --group-by topic \
  --folder .
```

## 🎯 Interview Preparation Features

- ✅ Only accepted solutions (no failed attempts)
- ✅ Real submission code (exactly what you submitted)
- ✅ Python language focused
- ✅ VS Code ready
- ✅ Git version controlled
- ✅ Topic organization available
- ✅ Consistent file formatting

## 🔍 Troubleshooting

### Common Issues:

1. **Command not found**: Make sure you're using the full Python path:

   ```bash
   /Users/joshrobertson8/projects/leetcode26/.venv/bin/python -m leetcode_export --help
   ```

2. **Authentication failed**: Your cookies may have expired. Get fresh cookies from the browser.

3. **No solutions exported**: Ensure you have accepted Python solutions on LeetCode.

### Getting Help:

```bash
/Users/joshrobertson8/projects/leetcode26/.venv/bin/python -m leetcode_export --help
```

## 📝 Next Steps for Interview Prep

1. **Review and annotate** each solution with time/space complexity
2. **Add comments** explaining the approach and key insights
3. **Create a study schedule** to revisit solutions regularly
4. **Group by company** if you're targeting specific companies
5. **Add test cases** for local validation

Happy coding! 🚀
