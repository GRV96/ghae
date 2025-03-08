import pytest

import json
from pathlib import Path

from syspathmodif import\
	sp_append,\
	sp_remove


_ENCODING_UTF8 = "utf-8"
_MODE_R = "r"

_LOCAL_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _LOCAL_DIR.parent


sp_append(_REPO_ROOT)
from ghae import\
	GitHubApiError,\
	detect_github_api_error
sp_remove(_REPO_ROOT)


def _load_whole_json_file(json_path):
	with json_path.open(mode=_MODE_R, encoding=_ENCODING_UTF8) as json_file:
		return json.load(json_file)


def test_error_detection_valid_request():
	response_data = _load_whole_json_file(
		_LOCAL_DIR/"response_to_valid_request.json")

	# Success if GitHubApiError is not raised.
	detect_github_api_error("No request for tests", response_data)


def test_error_detection_erroneous_request():
	response_data = _load_whole_json_file(
		_LOCAL_DIR/"response_to_erroneous_request.json")

	with pytest.raises(GitHubApiError):
		detect_github_api_error("No request for tests", response_data)
