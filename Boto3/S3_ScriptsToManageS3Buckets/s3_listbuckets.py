import boto3


ak = 'AKIATEYN5PTWUBCB2MMC'
sak = '1BO6iOP0sHgYd5cWV8T9zZVZ3FHWq/sptIc96aTm'

s3_client = boto3.client(
    service_name='s3',
    region_name='ap-south-1',
    aws_access_key_id=ak,
    aws_secret_access_key=sak,
)

response = s3_client.list_buckets()

buckets = response.get("Buckets")

for bucket in buckets:
    print(bucket['Name'])
    response = s3_client.list_objects(
    Bucket=bucket['Name'])
    print(response)

print(f" Total Buckets : {len(buckets)}")
print(buckets)