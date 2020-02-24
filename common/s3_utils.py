import boto3
from urlparse import urlparse

def split_s3_path(s3_path):
    o=urlparse(s3_path)
    print(o)
    return o.netloc, o.path[1:]

def copy_to_s3(dest,logs):
    bucket,key=split_s3_path(dest)
    print('bucket : %s and path : %s ' % (bucket, key))

    s3=boto3.resource('s3')
    for log in logs:
        filename=log.split("/")[-1]
        try:
            s3.meta.client.upload_file(filename, bucket, key+filename)
        except Exception as e:
            print(e)

# Delete File from s3 path
def delete_file(s3_path):
    client = boto3.client('s3')
    bucket, key = split_s3_path(s3_path)
    client.delete_object(Bucket=bucket, Key=key)