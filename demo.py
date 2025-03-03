"""
This script shows how function detect_github_api_error helps determining
whether a response from the GitHub API is the result of an erroneous request.
"""


from argparse import\
	ArgumentParser
import json
import requests
import sys

from ghae import\
	detect_github_api_error,\
	GitHubAPIError


def make_arg_parser():
	parser = ArgumentParser(description=__doc__)
	parser.add_argument("-r", "--repository",
		required=True,
		help="A GitHub repository's name in the form <owner>/<name>")

	return parser


args = make_arg_parser().parse_args()
repo_name = args.repository

# Request sending and response parsing
repo_url = f"https://api.github.com/repos/{repo_name}"
repo_response = requests.get(repo_url)
repo_data = json.loads(repo_response.content)

# Error detection
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
