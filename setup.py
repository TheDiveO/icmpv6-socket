#!/usr/bin/env python3

from setuptools import setup
from icmpv6socket import __version__
import os


with open(os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'README.md'
          )) as f:
    ldesc = f.read()

setup(
    name='icmpv6-socket',
    version=__version__,
    description='ICMPv6 socket convenience library',
    long_description=ldesc,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries'
    ],
    license='Apache License 2.0',
    author='TheDiveO',
    author_email='thediveo@gmx.eu',
    url='https://github.com/TheDiveO/linuxns_rel',
    packages=['icmpv6socket'],
    install_requires=[
    ],
    extras_require={
        'dev': [
            'coverage',
            'sphinx',
            'sphinx_rtd_theme'
        ]
    }
)
