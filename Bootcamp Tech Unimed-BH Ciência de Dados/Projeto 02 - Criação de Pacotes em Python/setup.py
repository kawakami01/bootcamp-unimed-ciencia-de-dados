from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing",
    version="0.0.3",
    author="Miguel Kawakami",
    description="Image Processing Package using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)