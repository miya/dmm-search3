from setuptools import setup, find_packages

setup(
    name='dmm_search3',
    version='0.3',
    description='DMM Web API v3.0 for Python3',
    url='https://github.com/0x0u/dmm',
    author='m0zu',
    author_email='m0zurillex@gmail.com',
    license='MIT',
    keywords='dmm',
    packages=find_packages(),
    install_requires=['requests==2.21.0'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=['Programming Language :: Python :: 3.6']
)
