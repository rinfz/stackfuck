#!/usr/bin/env python
""" Stackfuck Interpreter """
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md") as file_readme:
    readme = file_readme.read()

setup(
    name="Stackfuck",
    version="0.0.1",
    description="Interpreter for esoteric language Stackfuck",
    long_description=readme,
    author="fxcqz",
    license="MIT",
    url="https://github.com/fxcqz/stackfuck",
    packages=["stackfuck", "stackfuck.tests"],
    test_suite="stackfuck.tests",
)
