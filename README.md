# 🏆 GitHub Achievements Hunter

[![Automate Achievements](https://img.shields.io/badge/GitHub-Achievements-blueviolet?style=for-the-badge&logo=github)](https://github.com)
[![Pull Shark Tier 2](https://img.shields.io/badge/Pull_Shark-Silver_Tier_(16_PRs)-orange?style=for-the-badge&logo=git)](https://github.com)
[![YOLO Badge](https://img.shields.io/badge/YOLO-Ready-blueviolet?style=for-the-badge)](https://github.com)
[![Quickdraw Badge](https://img.shields.io/badge/Quickdraw-Ready-gold?style=for-the-badge)](https://github.com)
[![Pair Extraordinaire](https://img.shields.io/badge/Pair_Extraordinaire-Ready-blue?style=for-the-badge)](https://github.com)

A premium, sandboxed automation utility designed to quickly unlock, farm, and guide you through most of GitHub's profile achievements (badges) in a safe and standard-compliant way. 

---

## ⚡ Quick Start: Earn Your Badges Today

To get started, clone this repository (or run this on your local machine) and run the `hunter.py` script. The script uses a sandbox repository so your main profile code history remains pristine.

### 📋 Prerequisites

Make sure you have the following installed and configured on your machine:
* **Python 3.x**
* **Git** (configured with your name and email)
* **GitHub CLI (`gh`)** - logged in to your account.
  ```bash
  # Check login status
  gh auth status
  
  # Log in if you aren't already
  gh auth login
  ```

### 🚀 Running the Hunter Script

Run the automation script from the root folder:

```bash
python3 hunter.py
```

---

## 🛠️ How It Works: The Achievements

The hunter script sets up a temporary sandbox repository (`achievements-sandbox-<random_hex>`) and automates the following actions to trigger the badges on your profile:

| Achievement Badge | Target Action | Tier Automated | How it triggers |
| :--- | :--- | :--- | :--- |
| **Pull Shark** 🦈 | Merge pull requests into a default branch | **Silver (Tier 2)** | Script opens and merges **16 pull requests** sequentially. |
| **YOLO** 🪂 | Merge a pull request without code reviews | **Base Tier** | The script merges its own PRs without adding any reviewers. |
| **Quickdraw** ⚡ | Close an issue or PR within 5 minutes of creation | **Base Tier** | Script creates an issue and closes it within 2 seconds. |
| **Pair Extraordinaire** 👥 | Co-author a commit on a merged pull request | **Base Tier** | The script appends a `Co-authored-by` footer matching a verified GitHub bot on the first PR's commit. |

---

## 💡 Guide to Manual & Community Achievements

Some achievements cannot be fully automated using a single-user sandboxed script because they require community interaction, real sponsorship, or discussions. Here is how you can earn them:

### 🧠 Galaxy Brain
* **Requirement**: Have your answer marked as the accepted answer in a GitHub Discussion.
* **How to get it**:
  1. Go to any public repository that has **Discussions** enabled (you can enable it on this repo using `gh repo edit --enable-discussions` or via the repo settings web interface).
  2. Ask a question using a secondary GitHub account, or have a friend ask a question in your discussions.
  3. Reply to the question from your main account.
  4. Use the secondary account/friend's account to click **"Mark as answer"** on your reply.

### ⭐ Starstruck
* **Requirement**: Have one of your repositories starred by other users (Tiers: 1 star, 16 stars, 128 stars, etc.).
* **How to get it**:
  1. Share the link of your newly created repository with friends, colleagues, or communities.
  2. Ask them to drop a ⭐ on your repository. You only need **1 star** to unlock the base tier, and **16 stars** for the second tier!

### 💖 Public Sponsor
* **Requirement**: Sponsor someone on GitHub.
* **How to get it**:
  1. Visit [GitHub Sponsors](https://github.com/sponsors).
  2. Choose an open-source contributor or project you like.
  3. Sponsor them (some sponsors support tiers as low as $1/month).

---

> [!IMPORTANT]
> **Processing Time Delay:** GitHub's badge awarding system is asynchronous and runs on a periodic cron job. It typically takes **up to 24 hours** for newly earned achievements to reflect on your profile.

> [!WARNING]
> **Do Not Delete the Sandbox Repo Immediately:** If you delete the sandbox repository immediately after the script finishes, GitHub's achievement parser might not index the contributions in time. **Keep the sandbox repository active on your profile for at least 48 hours.** You can safely delete it afterwards.

---

*Made with ❤️ by [jayaprakashnarayana](https://github.com/jayaprakashnarayana)*
