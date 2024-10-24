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

## READING EXCEL FILE USING PANDAS AND CREATING FILE TOBE UPLOADED TO S3 BUCKET ##
df = pandas.read_excel("student_marks.xlsx")

dataset = pandas.DataFrame(df)

final_data = dataset.describe()

with open("student_marks.txt", "w") as f:
    f.write(str(final_data))

## PUT CREATED FILE TO S3 BUCKET ###

resource = s3_client.put_object(
    Body=str(final_data), # Data to be saved in S3 bucket should be typecasted to String, else it will throw error
    Bucket="uma-achukolu-boto3-bucket",
    Key="student_marks.txt",
)