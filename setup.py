from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="code-x",
    version="0.0.1",
    author="Wagner Eler do Couto",
    author_email="wagnereler@hotmmail.com",
    description="Crypt with Caesar's cipher",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wagnereler/code-x"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
)