#!/usr/bin/env python
import os
import re

from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')


requires = [
]


def get_version():
    init = open(os.path.join(ROOT, 'tiepy', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='tiepy',
    version=get_version(),
    description='Build time checker for maintainable, professional Python',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Mitchell Grice',
    url='https://github.com/gricey432/tiepy',
    packages=find_packages(exclude=['test*']),
    include_package_data=True,
    install_requires=[
        "click>=6.5",
        "dataclasses>=0.6; python_version < '3.7'",
    ],
    extras_require={
        "test": [
            "pytest",
        ]
    },
    entry_points={
        'console_scripts': [
            'tiepy = tiepy.cli:main'
        ]
    },
    python_requires='>=3.6',
    license="Apache License 2.0",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
