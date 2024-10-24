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

# # TO DOWNLOAD FIRST CSV FILE INTO PYTHON
s3.Bucket('bucket4you').download_file(Key='dataframe1.csv', Filename='s3_dataframe1.csv')


# # TO DOWNLOAD SECOND CSV FILE INTO PYTHON
s3.Bucket('bucket4you').download_file(Key='dataframe2.csv', Filename='s3_dataframe2.csv')

print(pandas.read_csv('s3_dataframe1.csv'))
print(pandas.read_csv('s3_dataframe2.csv'))