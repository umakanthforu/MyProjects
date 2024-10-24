import boto3
import os
import s3fs
import pandas


ak = 'AKIATEYN5PTWUBCB2MMC'
sak = '1BO6iOP0sHgYd5cWV8T9zZVZ3FHWq/sptIc96aTm'

s3 = boto3.resource(
    service_name='s3',
    region_name='ap-south-1',
    aws_access_key_id=ak,
    aws_secret_access_key=sak,
)

# prints the bucket names
for bucket in s3.buckets.all(): 
    print(bucket.name)
