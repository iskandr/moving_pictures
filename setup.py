#!/usr/bin/env python

from setuptools import setup, Extension

import sys

extension_modules = []
setup(
    name="images2movie",
    description="Create a movie from a sequence of images in Python (uses PIL and ffmpeg)"
    classifiers=['Development Status :: 3 - Alpha',
                 'Topic :: Software Development :: Libraries',
                 'License :: OSI Approved :: BSD License',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python :: 2.7',
                 ],
    author="Alex Rubinsteyn",
    author_email="alexr@cs.nyu.edu",
    license="BSD",
    version="0.1",
    url="http://github.com/iskandr/images2movie",
    packages=[ 'images2movie' ],
    package_dir={ '' : '.' },
    requires=[
      'numpy', 
      'scipy',
      'progressbar',
      'PIL', 
    ],
    ext_modules = extension_modules)
