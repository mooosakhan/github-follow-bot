
# GitHub Follower Increaser 🚀


This project helps you automatically follow users on GitHub to increase your followers. It targets users with large followings and follows them, allowing for a potential follow-back, helping you grow your GitHub presence. With this script, you can continuously follow users on multiple pages and boost your followers over time.

## 📢 Description

The **GitHub Follower Increaser** is a Python script that enables you to follow the followers of any GitHub user who has a large number of followers. By following users, there's a chance they may follow you back, thus growing your follower count.

- **How It Works**: 
  - The script fetches followers of a target GitHub user.
  - It follows each follower automatically.
  - You can paginate through results and keep following new users by increasing the page number.
  - The script runs continuously until you have followed enough users to achieve your desired number of followers.

This is a great way to grow your GitHub profile organically! By following users in the community, you're more likely to receive follow-backs.

## 📝 Features
- Automatically fetch and follow followers of a GitHub user.
- Support for paginating through multiple pages of followers.
- Easily increase your follower count over time.
- Requires no manual intervention once set up.

## 🔑 How to Get Your GitHub Personal Access Token (PAT)

To use the script, you'll need a **GitHub Personal Access Token (PAT)**. Here's how you can generate one:

1. Go to GitHub and log in to your account.
2. In the upper-right corner, click on your profile picture and select **Settings**.
3. In the left sidebar, click **Developer settings**.
4. Click **Personal access tokens**, then **Tokens (classic)**.
5. Click **Generate new token**.
6. Select the necessary scopes. For this script, you'll need at least the `user` scope.
7. Click **Generate token**.
8. Copy the token (you’ll need this for the script).

**Important**: Keep this token secure and never expose it publicly!

## 📦 Installation & Setup

### Prerequisites
- Python 3.x
- Required libraries (`requests`, `python-dotenv`)

### Installation Steps:
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/github-follower-increaser.git
   cd github-follow-bot
   ```

2. Install the required Python libraries:
   ```bash
   pip install requests python-dotenv
   ```

3. Create a `.env` file in the project root and add your GitHub Personal Access Token, the target GitHub user, and other settings:
   ```bash
   GITHUB_TOKEN=your_github_token
   TARGET_USER=your_target_user
   PER_PAGE=100
   PAGE=1
   ```

4. Add the `.env` file to `.gitignore` to ensure that your sensitive token is not uploaded to GitHub:
   ```bash
   echo .env >> .gitignore
   ```

## 🚀 Running the Script

Once the setup is complete, you're ready to start the script!

1. Simply run the script:
   ```bash
   python follow_bot.py
   ```

2. The script will:
   - Fetch the followers of the specified GitHub user.
   - Follow those users automatically.
   - Print the status of each follow attempt.
   
3. After one page of followers is processed, you can manually increase the page number in the `.env` file by 1 and run the script again to fetch the next page of followers. This process can be repeated as many times as you need to grow your follower count.

For example, after following the first 100 users:
- Change `PAGE=1` to `PAGE=2` and run the script again to follow users from pages 101-200.

### Example Commands to Increase Followers:
- Change the `PAGE` variable in `.env` to continue fetching followers from the next page:
  ```bash
  PAGE=2
  python follow_bot.py
  ```

- Repeat this process by increasing the page number and running the script until you reach your desired follower count!

## ❗ Important Notes:
- Make sure that your GitHub Personal Access Token (`GITHUB_TOKEN`) has the necessary permissions to follow users.
- Be cautious with rate limits—GitHub may temporarily block requests if you follow too many users too quickly. Ensure you follow at a reasonable pace to avoid hitting the limits.

## 🔧 Customize the Script
- You can adjust the number of results per page by changing the `PER_PAGE` value in the `.env` file (the default is 100).
- Modify the target user (`TARGET_USER`) to follow followers of different users with large followings.

## 🛡️ Security Reminder
**Never share your GitHub Personal Access Token publicly.** Always use `.env` files to keep sensitive data safe, and add `.env` to your `.gitignore` to prevent it from being committed to version control.

## 💬 Feedback and Issues
If you encounter any issues, feel free to open an issue on the GitHub repository. Your feedback is valuable for improving the script.

## 📄 License
MIT License

---

### 💡 Conclusion

The **GitHub Follower Increaser** script is a powerful tool to help you organically increase your follower count by following users in your targeted GitHub community. With the ability to paginate through follower pages, you can automate the process and gradually grow your presence on GitHub.

Happy coding and happy following! 😊


### Key Points:
- **Project Name**: GitHub Follower Increaser
- **Description**: Automatically follow followers of a GitHub user to grow your followers over time.
- **Token**: Use your GitHub Personal Access Token (PAT) to authenticate the script.
- **Pagination**: Manually increase the page number to fetch the next set of followers.
- **Security**: Store sensitive data in a `.env` file and keep it out of version control.

This `README.md` file provides a complete overview of your project, setup instructions, and usage details to ensure users understand how to use the script and where to find necessary information like their GitHub token.
