import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch values from the environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
TARGET_USER = os.getenv("TARGET_USER")
PER_PAGE = int(os.getenv("PER_PAGE", 100))  # Default to 100 if not provided
PAGE = int(os.getenv("PAGE", 1))  # Default to 1 if not provided

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_followers(user, page, per_page):
    """Fetch followers of a user."""
    url = f"https://api.github.com/users/{user}/followers"
    params = {"page": page, "per_page": per_page}
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()

def follow_user(username):
    """Follow a user by username."""
    url = f"https://api.github.com/user/following/{username}"
    response = requests.put(url, headers=HEADERS)
    if response.status_code == 204:
        print(f"Successfully followed {username}")
    else:
        print(f"Failed to follow {username}: {response.status_code} - {response.text}")

def main():
    try:
        # Fetch the next 100 followers
        followers = get_followers(TARGET_USER, PAGE, PER_PAGE)
        print(f"Found {len(followers)} followers on page {PAGE}.")

        # Follow each follower
        for follower in followers:
            username = follower["login"]
            follow_user(username)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
