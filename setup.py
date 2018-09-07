#! /usr/bin/env python

import setuptools
from html3.html3 import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="html3",
    version=__version__,
    description="simple, elegant HTML, XHTML and XML generation for python3 (based on html)",
    long_description=long_description,
    author="Pavel Liavonau",
    author_email="liavonlida@gmail.com",
    packages=setuptools.find_packages(),
    url='http://pypi.python.org/pypi/html3',
    project_urls={
        "Source Code": "https://github.com/pavelliavonau/html3/",
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: HTML',
        'License :: OSI Approved :: BSD License'
    ]

)
