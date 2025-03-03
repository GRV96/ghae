# __all__ declared at the module's end


from .github_api_error import\
	GitHubAPIError


_KEY_DOCUMENTATION_URL = "documentation_url"
_KEY_MESSAGE = "message"
_KEY_STATUS = "status"


def detect_github_api_error(request_url, api_data):
	if isinstance(api_data, dict):
		message = api_data.get(_KEY_MESSAGE)
		doc_url = api_data.get(_KEY_DOCUMENTATION_URL)
		status = api_data.get(_KEY_STATUS)

		if message is not None and doc_url is not None and status is not None:
			raise GitHubAPIError(message, doc_url, status, request_url)


__all__ = [detect_github_api_error.__name__]
