import os
import boto3
import s3fs
import pandas

ak = 'AKIATEYN5PTWUBCB2MMC'
sak = '1BO6iOP0sHgYd5cWV8T9zZVZ3FHWq/sptIc96aTm'

s3_client = boto3.client(
    service_name='s3',
    aws_access_key_id=ak,
    aws_secret_access_key=sak,
)

# DELETE AN OBJECT FROM S3 BUCKET

resource = s3_client.delete_object(
    Bucket="uma-achukolu-boto3-bucket",
    Key="student_marks.txt",
)