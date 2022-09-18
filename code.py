# first step :
import boto3


# ------------------------------------------------------------GET BUCKET NAMES------------------------------------------------------------------

# print out bucket names:
s3 = boto3.resource("s3")
for bucket in s3.buckets.all():
    print(bucket.name)
 ## output => sample-bucket-1801  

# ------------------------------------------------------------DOWNLOAD A FILE FROM BUCKET--------------------------------------------------------
# To download a file from an S3 bucket and immediately save it, we can use the download_file function:
# Create an S3 access object
s3 = boto3.client("s3")
s3.download_file(
    Bucket="sample-bucket-1801", Key="train.csv", Filename="data/downloaded_from_s3.csv"
)
# There won't be any output if the download is successful.
# You should pass the exact file path of the file to be downloaded to the Key parameter.
#  The Filename should contain the pass you want to save the file to.

# -------------------------------------------------------------UPLOAD A FILE TO A BUCKET----------------------------------------------------------

# Uploading is also very straightforward:
s3.upload_file(
    Filename="data/downloaded_from_s3.csv",
    Bucket="sample-bucket-1801",
    Key="new_file.csv",
)
# The function is upload_file and you only have to change the order of the parameters from the download function

# --------------------------------------------------------------GET LIST OF CONTENTS FORM BUCKET-----------------------------------------------

from boto3 import client

conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3
for key in conn.list_objects(Bucket='bucket_name')['Contents']:
    print(key['Key'])
# another way :
import boto3
s3 = boto3.resource('s3')

my_bucket = s3.Bucket('bucket_name')

for file in my_bucket.objects.all():
    print(file.key)
