"""
The demo shows how function detect_github_api_error helps determining whether a
response from the GitHub API is the result of an erroneous request. It also
constitutes an example of handling a GitHubApiError.

This script sends a request for a repository's data to the GitHub API. If the
request is valid, the script displays some information in the console.
"""


from argparse import\
	ArgumentParser,\
	RawDescriptionHelpFormatter
import json
import requests
import sys

from ghae import\
	GitHubApiError,\
	detect_github_api_error


def _make_arg_parser():
	parser = ArgumentParser(
		description=__doc__, formatter_class=RawDescriptionHelpFormatter)
	parser.add_argument("-r", "--repository",
		required=True,
		help="A GitHub repository's name in the form <owner>/<name>")

	return parser


args = _make_arg_parser().parse_args()
repo_name = args.repository

# Request sending and response parsing
repo_url = f"https://api.github.com/repos/{repo_name}"
repo_response = requests.get(repo_url)
repo_data = json.loads(repo_response.content)

# Error detection
try:
	detect_github_api_error(repo_url, repo_data)
except GitHubApiError as ge:
	print(ge)
	sys.exit(1)

id = repo_data.get("id")
name = repo_data.get("name")
full_name = repo_data.get("full_name")
description = repo_data.get("description")
language = repo_data.get("language")
fork = repo_data.get("fork")
visibility = repo_data.get("visibility")
topics = repo_data.get("topics")

print(f"Request: {repo_url}\n")
print("Repository data")
print(f"ID: {id}")
print(f"Name: {name}")
print(f"Full name: {full_name}")
print(f"Description: {description}")
print(f"Language: {language}")
print(f"Fork: {fork}")
print(f"Visibility: {visibility}")
print(f"Topics: {topics}")
