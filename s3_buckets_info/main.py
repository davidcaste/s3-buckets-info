#!/usr/bin/env python
"""
s3-buckets-info analyzes S3 buckets

Usage:
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


def main():
    args = docopt.docopt(__doc__)

    if args['--version']:
        print('s3-buckets-info {}'.format(__version__))
        return


if __name__ == '__main__':
    main()
