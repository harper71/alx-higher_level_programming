#!/usr/bin/python3
"""
advanced task 
"""
import requests
import sys


def get_commits(repo, owner):
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f'{sha}: {author_name}')
    else:
        print(f'Failed to retrieve commits: {response.status_code}')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <repository_name> <owner_name>")
    else:
        repo = sys.argv[1]
        owner = sys.argv[2]
        get_commits(repo, owner)
