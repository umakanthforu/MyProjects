import os
import boto3
import s3fs

ak = 'AKIATEYN5PTWUBCB2MMC'
sak = '1BO6iOP0sHgYd5cWV8T9zZVZ3FHWq/sptIc96aTm'

s3_client = boto3.client(
    service_name = 's3',
    aws_access_key_id = ak,
    aws_secret_access_key = sak,
)

### TO GET THE LIST OF BUCKETS PRINTED AND STORED AS A LIST ###

resource = s3_client.list_buckets() #command to save output to resource variable

bucket_details = resource.get("Buckets") # filtering bucket details from output

listofbuckets = [] # declaring an empty set to store bucket names

for item in bucket_details:
    x = item.get("Name")
    print(x)
    listofbuckets.append(x)

# print("The details of buckets are :", listofbuckets) # all the names are stored in empty list defined.

## TO SEE THE LIST OF OBJECTS IN THE BUCKETS ##

for item1 in listofbuckets:
    print(f"The list of items in Bucket {item1} are  :")
    resource1 = s3_client.list_objects(
        Bucket=item1,
    )
    object_details = resource1.get("Contents")
    if object_details == None:
        print("No objects in this Bucket")
    else:
        for item10 in object_details:
            print(item10.get("Key"))
        
  



