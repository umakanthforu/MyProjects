import boto3
import s3fs
import pandas


s3_client = boto3.client(
    service_name = "s3"
)

# resource = s3_client.create_bucket(
#     Bucket = "umakanth-achukolu-creation-2024",
#     CreateBucketConfiguration = {
#         "LocationConstraint" : "ap-south-1"
#     }
# )

# presource = pandas.read_excel("Managing_S3_using_BOTO3\\student_marks.xlsx")

# dataframe = pandas.DataFrame(presource)


# dataframe["Total"]= dataframe["English"]+dataframe["Hindi"]+dataframe["Telugu"]+dataframe["Maths"]+dataframe["Science"]+dataframe["Social"]

# dataframe.to_excel("C:\\Users\\kanth\\OneDrive\\Desktop\\Trial\\myfile.xlsx", index=False)

# s3resource = s3_client.put_object(
#     Body = str(dataframe),
#     Bucket = "umakanth-achukolu-creation-2024",
#     Key = "my_dataframe.xlsx"
# )

# resource = s3_client.get_object(
#     Bucket = "umakanth-achukolu-creation-2024",
#     Key = "my_dataframe.xlsx"
# )

# downloadfile = resource.get("Body").read().decode()
# # print(downloadfile)

# with open("downloadedfile_s3.xlsx", "w") as f:
#     f.write(downloadfile)

# resource = s3_client.delete_object(
#     Bucket = "umakanth-achukolu-creation-2024",
#     Key = "my_dataframe.xlsx"
# )

resource = s3_client.delete_bucket(
    Bucket = "umakanth-achukolu-creation-2024"
)