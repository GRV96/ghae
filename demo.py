import json
import requests
import sys

from ghae import\
	detect_github_api_error,\
	GitHubAPIError


try:
	repo_name = sys.argv[1]
except IndexError:
	print("Provide a GitHub repository's name in the format <owner>/<name> as an argument.")
	sys.exit(1)

repo_url = f"https://api.github.com/repos/{repo_name}"
repo_response = requests.get(repo_url)
repo_data = json.loads(repo_response.content)

try:
	detect_github_api_error(repo_url, repo_data)
except GitHubAPIError as ge:
	print(ge)
	sys.exit(1)

id = repo_data.get("id")
full_name = repo_data.get("full_name")
description = repo_data.get("description")
fork = repo_data.get("fork")
visibility = repo_data.get("visibility")
topics = repo_data.get("topics")

print("Repository data")
print(f"Full name: {full_name}")
print(f"ID: {id}")
print(f"Description: {description}")
print(f"Fork: {fork}")
print(f"Visibility: {visibility}")
print(f"Topics: {topics}")
