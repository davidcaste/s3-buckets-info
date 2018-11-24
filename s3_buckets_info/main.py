#!/usr/bin/env python
"""
s3-buckets-info analyzes S3 buckets

Usage:
  s3-buckets-info [--json] [BUCKET_NAME...]
  s3-buckets-info -h | --help
  s3-buckets-info -v | --version

General options:
  --json        Print output in json format
  -h --help     Show this help message and exit
  -v --version  Show program version and exit
"""

from __future__ import (absolute_import, division, print_function, unicode_literals)
__metaclass__ = type

import json

import docopt
import humanize

from s3_buckets_info import __version__
from s3_buckets_info.analyzer import analyze_buckets


def main():
    args = docopt.docopt(__doc__)

    if args['--version']:
        print('s3-buckets-info {}'.format(__version__))
        return

    if args['--json']:
        get_output = _get_json_output
    else:
        get_output = _get_human_output

    try:
        for bucket_info in analyze_buckets(args['BUCKET_NAME']):
            print(get_output(bucket_info))
    except Exception as e:
        raise SystemExit('Unknown error: {}.'.format(e.message))


def _get_human_output(bucket_info):
    size = humanize.naturalsize(bucket_info['objects_size'])

    return '''
Bucket "{b[name]}":
  Created at: {b[creation_date]}
  Number of files: {b[objects_num]}
  Total size of files: {objects_size}'''.format(b=bucket_info, objects_size=size)


def _get_json_output(bucket_info):
    return json.dumps(bucket_info, default=str)


if __name__ == '__main__':
    main()
