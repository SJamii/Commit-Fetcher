import requests
from datetime import datetime


def fetch_commits(repo, max_commits=10):
    """
    Fetch commits from a GitHub repository
    :param repo: repository in format 'owner/repo'
    :param max_commits: maximum number of commits to fetch
    """
    api_url = f"https://api.github.com/repos/{repo}/commits"
    headers = {}

    try:
        response = requests.get(api_url, headers=headers, params={'per_page': max_commits})
        response.raise_for_status()

        commits = response.json()
        print(f"\nLatest commits from {repo}:")
        print("-" * 50)

        for commit in commits:
            author = commit['commit']['author']['name']
            message = commit['commit']['message'].split('\n')[0]  # Get first line of commit message
            date = datetime.strptime(commit['commit']['author']['date'],
                                     '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')

            print(f"Author: {author}")
            print(f"Date: {date}")
            print(f"Message: {message}")
            print("-" * 50)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching commits: {e}")


if __name__ == "__main__":
    REPOSITORY = "microsoft/vscode"
    fetch_commits(REPOSITORY)