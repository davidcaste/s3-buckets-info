#!/usr/bin/env python

from setuptools import setup

from s3_buckets_info import __version__
setup(
    name='s3-buckets-info',
    version=__version__,
    description='Yet another S3 analysis tool',
    url='TBD',
    author='John Doe',
    author_email='john_doe@foo.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
    packages=['s3_buckets_info'],
    install_requires=[
        'boto3',
        'docopt',
        'humanize'
    ],
    extras_require={
        'develop': ['ipython', 'pylint']
    },
    entry_points={
        'console_scripts': [
            's3-buckets-info = s3_buckets_info.main:main'
        ]
    }
)

