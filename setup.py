from setuptools import setup, find_packages

install_requires = [line.strip() for line in open("requirements.txt").readlines()]

setup(
    name="dmm-search3",
    version="2.2",
    description="DMM Web API Version 3.0 Wrapper for Python3",
    url="https://github.com/miya/dmm-search3",
    author="miya",
    author_email="m0zurillex@gmail.com",
    license="MIT",
    keywords=["python3", "dmm", "REST API"],
    packages=find_packages(),
    install_requires=install_requires,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=["Programming Language :: Python :: 3.7"]
)
