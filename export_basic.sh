#!/bin/bash

# LeetCode Basic Export Script
# Exports all accepted Python solutions to the current directory

echo "🚀 LeetCode Basic Export"
echo "======================="
echo ""
echo "This will export all your accepted Python solutions to the current directory."
echo ""
echo "You need to provide your LeetCode cookies from the browser."
echo ""
echo "Steps to get cookies:"
echo "1. Open leetcode.com and log in"
echo "2. Open DevTools (Cmd+Option+I)"
echo "3. Go to Network tab"
echo "4. Refresh the page"
echo "5. Click any leetcode.com request"
echo "6. Copy the entire Cookie header value"
echo ""
echo -n "Paste your LeetCode cookies here: "
read -r cookies

if [ -z "$cookies" ]; then
    echo "❌ Error: No cookies provided. Exiting."
    exit 1
fi

echo ""
echo "🔄 Starting export..."
echo ""

/Users/joshrobertson8/projects/leetcode26/.venv/bin/python -m leetcode_export \
  --cookies "$cookies" \
  --only-accepted \
  --language python \
  --folder .

echo ""
echo "✅ Export completed!"
echo ""
echo "Next steps:"
echo "1. Run ./format_solutions.py to add consistent headers"
echo "2. Run 'git add .' and 'git commit -m \"Import LeetCode solutions\"'"
echo ""