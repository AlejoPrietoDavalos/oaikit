from pathlib import Path
from setuptools import find_packages, setup

setup(
    name = "oaikit",
    version = "0.0.4",
    author = "Alejo Prieto Dávalos",
    author_email = "alejoprietodavalos@gmail.com",
    packages = find_packages(),
    description = "Python wrapper for OpenAI API.",
    long_description = Path("README.md").read_text(),
    long_description_content_type = "text/markdown",
    url = "https://pypi.org/project/oaikit/",
    project_urls = {
        "Source": "https://github.com/AlejoPrietoDavalos/oaikit/"
    },
    python_requires = ">=3.11",
    install_requires = [
        "pydantic>=2.8",
        "openai>=1.35.13"
    ],
    include_package_data = True
)
