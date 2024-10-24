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

# TO CHECK HOW MANY FILES ARE THERE
# for obj in s3.Bucket('bucket4you').objects.all():
#     print(obj)

# TO READ FIRST CSV FILE INTO PYTHON
s3_read1 = s3.Bucket('bucket4you').Object('dataframe1.csv').get()
s3_dataframe1 = pandas.read_csv(s3_read1['Body'], index_col=0)

print(s3_dataframe1)


# TO READ SECOND CSV FILE INTO PYTHON
s3_read2 = s3.Bucket('bucket4you').Object('dataframe2.csv').get()
s3_dataframe2 = pandas.read_csv(s3_read2['Body'], index_col=0)

print(s3_dataframe2)
