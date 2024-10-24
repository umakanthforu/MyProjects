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
# ## CODE TO CREATE A NEW BUCKET ###
# resource = s3_client.create_bucket(
#     Bucket="uma-achukolu-boto3-bucket", ## NAME OF NEW BUCKET(SHOULD BE UNIQUE)
#     CreateBucketConfiguration={
#         'LocationConstraint': 'ap-south-1' ## REGION OF NEW BUCKET
#         }
# )

