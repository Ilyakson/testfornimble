import boto3
from config import S3_BUCKET, S3_KEY, S3_SECRET


def get_s3_resource():
    return boto3.resource(
        "s3",
        aws_access_key_id=S3_KEY,
        aws_secret_access_key=S3_SECRET
    )


def get_bucket():
    s3_resource = get_s3_resource()
    return s3_resource.Bucket(S3_BUCKET)
