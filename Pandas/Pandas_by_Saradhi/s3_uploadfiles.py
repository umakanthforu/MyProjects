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

# defining dataframes
dataframe1 = pandas.DataFrame({'x':[1,2,3], 'y':['a','b','c']})
dataframe2 = pandas.DataFrame({'x':[101,202,303], 'y':['ant','ball','cat']})

# saving dataframes to csv files
dataframe1.to_csv('dataframe1.csv')
dataframe2.to_csv('dataframe2.csv')

# print(dataframe1, dataframe2)

# for uploding files to s3 bucket
s3.Bucket('bucket4you').upload_file(Filename='dataframe1.csv', Key='dataframe1.csv')
s3.Bucket('bucket4you').upload_file(Filename='dataframe2.csv', Key='dataframe2.csv')

# TO CHECK HOW MANY FILES ARE THERE
for obj in s3.Bucket('bucket4you').objects.all():
    print(obj)

