# coding: utf-8

try:
    import setuptools
    from setuptools import setup, find_packages
except ImportError:
    print("Please install setuptools.")

import os
long_description = 'Python implementation of the Apriori Algorithm.'
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()

setup(
    name  = 'akapriori',
    version = '0.1.0',
    description = 'Python implementation of the Apriori Algorithm.',
    long_description = long_description,
    license = 'MIT',
    author = 'Akihiro Kondo',
    author_email = 'akihirokondo511@gmail.com',
    url = 'https://github.com/aknd/akapriori',
    keywords = 'apriori',
    packages = find_packages(),
    install_requires = [],
    classifiers = [
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3.5',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: MIT License'
    ]
)
