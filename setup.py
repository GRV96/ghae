import setuptools


_ENCODING_UTF8 = "utf-8"
_MODE_R = "r"


def _make_long_description():
	with open("README.md", _MODE_R, encoding=_ENCODING_UTF8) as readme_file:
		readme_content = readme_file.read()

	title_fr = "## FRANÇAIS"
	title_en = "## ENGLISH"

	index_fr = readme_content.index(title_fr)
	index_end_fr = readme_content.index("### Dépendances")

	index_en = readme_content.index(title_en)
	index_desc_en = index_en + len(title_en)
	index_desc_end_en = readme_content.index("### Content", index_desc_en)
	index_end_en = readme_content.index("### Dependencies", index_desc_end_en)

	long_description = readme_content[index_fr: index_end_fr]\
		+ readme_content[index_en:index_end_en].strip()

	return long_description


if __name__ == "__main__":
	long_desc = _make_long_description()
	short_desc = "Exception GitHubApiError can be raised when a request to the GitHub API fails."

	setuptools.setup(
		name = "ghae",
		version = "0.0.0",
		author = "Guyllaume Rousseau",
		description = short_desc,
		long_description = long_desc,
		long_description_content_type = "text/markdown",
		url = "https://github.com/GRV96/ghae",
		classifiers = [
			"Private :: Do Not Upload", # Remove when ready to publish.
			"Development Status :: 5 - Production/Stable",
			"Intended Audience :: Developers",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
			"Programming Language :: Python :: 3",
			"Topic :: Software Development :: Libraries",
			"Topic :: Software Development :: Version Control :: Git",
			"Topic :: Utilities"
		],
		packages = setuptools.find_packages(
			exclude=(".github",)),
		license = "MIT",
		license_files = ("LICENSE",))
