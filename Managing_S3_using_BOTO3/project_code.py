import pandas
import s3fs
import boto3

ak = 'AKIATEYN5PTWUBCB2MMC'
sak = '1BO6iOP0sHgYd5cWV8T9zZVZ3FHWq/sptIc96aTm'

s3_client = boto3.client(
    service_name = 's3',
    aws_access_key_id = ak,
    aws_secret_access_key = sak,
)

data = pandas.read_excel("student_marks.xlsx")

mydata = pandas.DataFrame(data)

final_data = mydata.describe()
final_data1 = mydata.loc[0:10, "Social"]

# with open("testdata.txt", "w") as f:
#     f.write(str(final_data1))

with open("testdata.txt" , "r") as f:
    final_data2 = f.read()


# to upload file to s3 bucket
resource = s3_client.put_object(
    Body=str(final_data2),
    Bucket="aws-s3-umakanth-achukolu",
    Key="test_data.txt",
)

