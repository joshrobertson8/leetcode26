#!/bin/bash

# Quick setup script for LeetCode solutions export
# Run this after exporting to quickly set up the repository

echo "🔧 Setting up LeetCode Solutions Repository"
echo "==========================================="

# Set up git user if not already configured
if ! git config user.email > /dev/null 2>&1; then
    echo "⚙️  Setting up Git configuration..."
    echo -n "Enter your Git email: "
    read -r git_email
    echo -n "Enter your Git username: "
    read -r git_name
    
    git config user.email "$git_email"
    git config user.name "$git_name"
    echo "✅ Git configuration set"
fi

# Create initial commit with the setup files
echo "📝 Creating initial commit..."
git add README.md .gitignore export_basic.sh export_grouped.sh format_solutions.py setup_repo.sh
git commit -m "Initial setup: Add LeetCode export tools and documentation"

echo ""
echo "✅ Repository setup complete!"
echo ""
echo "🚀 Next steps:"
echo "1. Run './export_basic.sh' or './export_grouped.sh' to import your solutions"
echo "2. Run 'python format_solutions.py' to format the imported solutions"  
echo "3. Review and commit your solutions"
echo ""
echo "📚 Quick commands:"
echo "   ./export_basic.sh      # Export to flat structure"
echo "   ./export_grouped.sh    # Export organized by topic"
echo "   python format_solutions.py  # Add headers and formatting"
echo ""