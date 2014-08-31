#!/usr/bin/env python
from setuptools import setup

ENTRY_POINTS = """
[console_scripts]
sams = sams:main
"""

setup(
    name="SAMS Client",
    version="0.0.0",
    author="Britt Gresham",
    author_email="brittcgresham@gmail.com",
    description=(""),
    license="MIT",
    install_requires=[
        'docopt',
        'protobuf',
    ],
    entry_points=ENTRY_POINTS,
)
