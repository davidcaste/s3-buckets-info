from __future__ import (absolute_import, division, print_function, unicode_literals)
__metaclass__ = type

import sys

import boto3
from botocore.exceptions import ClientError


def analyze_buckets(buckets):
    if len(buckets) == 0:
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        bucket_names = [i['Name'] for i in response['Buckets']]
    else:
        bucket_names = buckets

    for name in bucket_names:
        try:
            yield _get_bucket_info(name)
        except ClientError as e:
            print('Error analyzing bucket "{}": {}.'.format(name, e.message), file=sys.stderr)


def _get_bucket_info(name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(name)

    objects_num = 0
    objects_size = 0

    for obj in bucket.objects.all():
        objects_num += 1
        objects_size += obj.size

    bucket_info = {
        'name': name,
        'creation_date': bucket.creation_date,
        'objects_num': objects_num,
        'objects_size': objects_size
    }

    return bucket_info



