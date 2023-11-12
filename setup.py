from setuptools import setup, find_packages
import os

with open('./README.md','r') as f:
    long_description = f.read()

VERSION = '0.1'
DESCRIPTION = 'Math Quiz Package'
LONG_DESCRIPTION = 'This is math quiz package where user enter input and this app will return output and check user answer and own answer and assign scores'

# Setting up
setup(
    name="math-quiz",
    version=VERSION,
    author="Haaris (Haaris Iqubal)",
    author_email="<haaris.iqubal@fau.de>",
    license="Apache",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/HaarisIqubal/dsss_homework_2/',
    packages=find_packages(where='math_quiz'),
    keywords=['math quiz'],
    classifiers=[
        "Development Status :: 1 - Final",
        "Intended Audience :: User",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.8.7",
)