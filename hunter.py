#!/usr/bin/env python3
import os
import sys
import time
import random
import string
import shutil
import subprocess

def run_command(cmd, cwd=None, capture_output=True, text=True):
    """Utility function to run shell commands safely."""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            stdout=subprocess.PIPE if capture_output else None,
            stderr=subprocess.PIPE if capture_output else None,
            shell=True,
            check=True,
            text=text
        )
        return result.stdout.strip() if capture_output else ""
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error executing command: {cmd}")
        if capture_output:
            print(f"Stdout: {e.stdout}")
            print(f"Stderr: {e.stderr}")
        raise e

def print_banner():
    print("=" * 60)
    print(" 🏆  GITHUB ACHIEVEMENTS HUNTER - AUTOMATION SANDBOX  🏆")
    print("=" * 60)
    print("This script will automate the following achievements:")
    print("  ✓ YOLO (Merge pull request without code review)")
    print("  ✓ Quickdraw (Close issue and PR within 5 minutes)")
    print("  ✓ Pair Extraordinaire (Co-author a commit on a merged PR)")
    print("  ✓ Pull Shark (Merge 16 Pull Requests to earn Tier 2)")
    print("-" * 60)

def main():
    print_banner()

    # 1. Verify gh CLI installation and authentication
    print("🔍 Checking prerequisites...")
    if not shutil.which("git"):
        print("❌ Git is not installed or not in PATH.")
        sys.exit(1)
    if not shutil.which("gh"):
        print("❌ GitHub CLI (gh) is not installed or not in PATH.")
        print("💡 Please install it via Homebrew: brew install gh")
        sys.exit(1)

    try:
        username = run_command("gh api user -q .login")
        print(f"✅ Authenticated as: {username}")
    except Exception:
        print("❌ Not authenticated with gh CLI. Please run 'gh auth login' first.")
        sys.exit(1)

    # 2. Setup paths and unique sandbox name
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    sandbox_repo_name = f"achievements-sandbox-{random_suffix}"
    user_home = os.path.expanduser("~")
    sandbox_path = os.path.join(user_home, sandbox_repo_name)

    print(f"📂 Creating sandbox repository locally at: {sandbox_path}")
    os.makedirs(sandbox_path, exist_ok=True)

    try:
        # 3. Initialize Git sandbox repo
        print("🏗️ Initializing Git sandbox...")
        run_command("git init -b main", cwd=sandbox_path)
        
        # Configure local git user if not configured globally, otherwise reuse global config
        try:
            user_email = run_command("git config --global user.email")
            user_name = run_command("git config --global user.name")
        except Exception:
            # Fallbacks if global git user is not configured
            run_command(f'git config user.email "{username}@users.noreply.github.com"', cwd=sandbox_path)
            run_command(f'git config user.name "{username}"', cwd=sandbox_path)

        with open(os.path.join(sandbox_path, "README.md"), "w") as f:
            f.write(f"# Achievements Sandbox ({sandbox_repo_name})\n\nThis is a temporary repository generated to earn GitHub achievements.\n")

        run_command("git add README.md", cwd=sandbox_path)
        run_command('git commit -m "Initial commit"', cwd=sandbox_path)

        # 4. Create GitHub repository using gh CLI
        print(f"🚀 Creating GitHub repository: {username}/{sandbox_repo_name}...")
        run_command(f"gh repo create {sandbox_repo_name} --public --source=. --remote=origin --push", cwd=sandbox_path)
        
        # Enable discussions (useful for Galaxy Brain guidelines)
        print("💬 Enabling Discussions on sandbox repo...")
        run_command(f"gh repo edit --enable-discussions", cwd=sandbox_path)

        # 5. Quickdraw Issue Automation
        print("\n🎯 Triggering Issue Quickdraw...")
        issue_out = run_command(
            'gh issue create --title "Quickdraw Badge Verification" --body "Testing GitHub Quickdraw achievement. This issue will be closed immediately."',
            cwd=sandbox_path
        )
        # Parse issue URL to find issue number (usually ends with /issues/<num>)
        issue_number = issue_out.split("/")[-1]
        print(f"   Created Issue #{issue_number}. Closing it now...")
        time.sleep(2)  # Short pause to ensure distinct creation/close events
        run_command(f"gh issue close {issue_number}", cwd=sandbox_path)
        print("   Issue closed successfully!")

        # 6. YOLO + Pair Extraordinaire + Pull Shark (16 PRs)
        total_prs = 16
        print(f"\n🌊 Starting Pull Request loop to farm Pull Shark Tier 2 ({total_prs} PRs)...")
        print("This will also trigger Pair Extraordinaire and YOLO on the first PR.")
        
        for i in range(1, total_prs + 1):
            branch_name = f"achievement-farm-{i}"
            print(f"\n🔄 PR {i}/{total_prs}: Processing...")

            # Create branch
            run_command(f"git checkout -b {branch_name}", cwd=sandbox_path)

            # Update file
            with open(os.path.join(sandbox_path, "pullshark.txt"), "a") as f:
                f.write(f"Pull Request #{i} merged.\n")

            run_command("git add pullshark.txt", cwd=sandbox_path)

            # For the first commit, co-author with github-actions[bot] to trigger Pair Extraordinaire
            if i == 1:
                print("   👥 Co-authoring commit with github-actions[bot] for Pair Extraordinaire...")
                commit_msg = (
                    "Farming achievements - PR 1\n\n"
                    "Co-authored-by: github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>"
                )
                # Escape double quotes in commit message
                commit_msg_escaped = commit_msg.replace('"', '\\"')
                run_command(f'git commit -m "{commit_msg_escaped}"', cwd=sandbox_path)
            else:
                run_command(f'git commit -m "Farming achievements - PR {i}"', cwd=sandbox_path)

            # Push branch
            run_command(f"git push origin {branch_name}", cwd=sandbox_path)

            # Open PR
            print(f"   📤 Creating PR #{i}...")
            run_command(
                f'gh pr create --title "Automated Achievement Pull Request #{i}" --body "Automating Pull Shark farming. PR {i}/{total_prs}." --base main --head {branch_name}',
                cwd=sandbox_path
            )

            # Merge PR (triggers YOLO and Quickdraw)
            print(f"   📥 Merging PR #{i}...")
            # We use --merge to perform standard merge, and -d to delete branch
            run_command(f"gh pr merge --merge --delete-branch", cwd=sandbox_path)

            # Go back to main and pull updates
            run_command("git checkout main", cwd=sandbox_path)
            run_command("git pull origin main", cwd=sandbox_path)
            
            # Clean up local tracking branch
            try:
                run_command(f"git branch -D {branch_name}", cwd=sandbox_path)
            except Exception:
                pass

        print("\n" + "=" * 60)
        print(" 🎉  SANDBOX AUTOMATION COMPLETED SUCCESSFULLY!  🎉")
        print("=" * 60)
        print(f"Sandbox Repository: https://github.com/{username}/{sandbox_repo_name}")
        print("\n⚠️  IMPORTANT NOTE:")
        print("GitHub's achievements backend processing runs periodically and can take up to 24 hours.")
        print("Do NOT delete the sandbox repository or its branches immediately. Keep it active for")
        print("at least 48 hours to ensure GitHub rewards you with the badges:")
        print("  - Pull Shark (Tier 2)")
        print("  - YOLO")
        print("  - Quickdraw")
        print("  - Pair Extraordinaire")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Run failed: {e}")
        print("Attempting to restore main branch context...")
    
if __name__ == "__main__":
    main()
