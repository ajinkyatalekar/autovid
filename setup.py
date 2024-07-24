from setuptools import setup, find_packages
import os

VERSION = '0.0.1'
DESCRIPTION = 'Generate Reddit Text-to-Speech videos'
LONG_DESCRIPTION = 'A package that allows to quickly create videos from raw text or fetching reddit posts and comments.'

# Setting up
setup(
    name="autovid",
    version=VERSION,
    author="Ajinkya Talekar",
    author_email="ajinkyat@buffalo.edu",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['selenium', 'moviepy', 'gtts', 'praw'],
    keywords=['python', 'reddit', 'tts', 'video generator', 'automation'],
    classifiers=[
        "Development Status :: 2 - Development",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)