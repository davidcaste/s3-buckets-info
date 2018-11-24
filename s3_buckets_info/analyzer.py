from __future__ import (absolute_import, division, print_function, unicode_literals)
__metaclass__ = type

import boto3


def analyze_buckets():
    client = boto3.client('s3')
    response = client.list_buckets()

    for bucket in response['Buckets']:
        objects_num, objects_size = _get_bucket_info(bucket['Name'])

        bucket_info = {
            'name': bucket['Name'],
            'creation_date': bucket['CreationDate'],
            'objects_num': objects_num,
            'objects_size': objects_size
        }

        yield bucket_info


def _get_bucket_info(name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(name)

    objects_num = 0
    objects_size = 0

    for obj in bucket.objects.all():
        objects_num += 1
        objects_size += obj.size

    return objects_num, objects_size



