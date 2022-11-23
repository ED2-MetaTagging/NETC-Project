import boto3
from flask import session

ACCESS_KEY = 'AKIAQ4D4US5BPC2UQRS2'
SECRET_KEY = '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'

BUCKET_NAME = 'netc-filestorage'

def _get_s3_resource():
        return boto3.resource(
            's3',
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY
        )
   


def get_bucket():
    s3_resource = _get_s3_resource()
    if 'bucket' in session:
        bucket = session['bucket']
    else:
        bucket = BUCKET_NAME

    return s3_resource.Bucket(bucket)

