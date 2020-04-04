from setuptools import setup, find_packages

install_reqs = [line.strip() for line in open("requirements.txt").readlines()]

setup(
    name="dmm_search3",
    version="2.1",
    description="DMM Web API Version 3.0 Wrapper for Python3",
    url="https://github.com/miya/dmm_search3",
    author="miya",
    author_email="m0zurillex@gmail.com",
    license="MIT",
    keywords="Python3 dmm API",
    packages=find_packages(),
    install_requires=install_reqs,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=["Programming Language :: Python :: 3.7"]
)
