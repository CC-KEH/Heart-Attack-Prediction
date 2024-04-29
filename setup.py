import setuptools


with open('README.md', 'r') as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = 'Project-4'
SRC_REPO = 'src'
AUTHOR_NAME = 'CC-KEH'
AUTHOR_EMAIL = 'example@example.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description='Project 4',
    long_description=long_description,
    url=f"https/github.com/{AUTHOR_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src')
)
