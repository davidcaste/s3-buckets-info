#!/usr/bin/env python
"""
s3-buckets-info analyzes S3 buckets

Usage:
  s3-buckets-info
  s3-buckets-info -h | --help
  s3-buckets-info -v | --version

General options:
  -h --help     Show this help message and exit
  -v --version  Show program version and exit
"""

from __future__ import (absolute_import, division, print_function, unicode_literals)
__metaclass__ = type

import docopt

from s3_buckets_info import __version__
from s3_buckets_info.analyzer import analyze_buckets


def main():
    args = docopt.docopt(__doc__)

    if args['--version']:
        print('s3-buckets-info {}'.format(__version__))
        return

    for bucket_info in analyze_buckets():
        print('''
Bucket "{name}":
  Created at: {creation_date}
  Number of files: {objects_num}
  Total size of files: {objects_size}'''.format(**bucket_info))


if __name__ == '__main__':
    main()
