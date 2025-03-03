from .api_error_detection import\
	detect_github_api_error
from .github_api_error import\
	GitHubAPIError


__all__ = [
	detect_github_api_error.__name__,
	GitHubAPIError.__name__
]
