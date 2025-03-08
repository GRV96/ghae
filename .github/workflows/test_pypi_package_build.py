"""
This script is meant to run on GitHub's virtual machine ubuntu-latest in a CI
workflow. It builds the PyPI package and installs it to ensure that the package
works. However, the script does not upload the package to PyPI.
"""


from os import system
from pathlib import Path


repo_root = Path(__file__).resolve().parents[2]

system(f"python3 {repo_root}/setup.py sdist")

src_dist = next((repo_root/"dist").glob("ghae-*.tar.gz"))

system(f"pip3 install --no-cache-dir {src_dist}")
