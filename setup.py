#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "pandas",
    "numpy",
    "scipy",
    "matplotlib",
    "plotly",
    "networkx",
]


'''
Check if WNTR is installed, 
Currently, the install over at WNTR is changing
Must install it first manually before this. 
'''

try:
    import wntr
    if wntr.__version__!="0.5.0":
        raise ModuleNotFoundError(f"WNTR version 0.5.0 module not found. {wntr.__version__} version found instead.")
except ModuleNotFoundError:
    raise ModuleNotFoundError("WNTR module not found. Install version 0.5.0 before this package. ")

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest",
]

setup(
    author="Lu Xing",
    author_email="xinglu@utexas.edu",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    description="tsnet conducts transient simulation using MOC method for water distribution systems.",
    entry_points={},
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="tsnet",
    name="tsnet",
    packages=find_packages(),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/glorialulu/TSNet",
    version="0.2.4",
    zip_safe=False,
)
