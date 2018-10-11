#!/usr/bin/python
# -*- coding: utf-8 -*-

"""A tool to extract data from html table
"""
from setuptools import setup

setup(
    name='htmltable-df',
    url='https://github.com/shiaukuan/htmltable-df',
    version='1.0.2',
    author='shiaukuan',
    author_email='kuan60508@gmail.com',
    description='A python library for extracting data from html table',
    license='MIT',
    keywords='html table pyquery crawler scrape',
    packages=[
        'htmltable_df',
    ],
    install_requires=[
        'pyquery',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
