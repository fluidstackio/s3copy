import boto3
from botocore.exceptions import NoCredentialsError
import sys
import os

ACCESS_KEY = os.getenv("ACCESS_KEY", default=None)
SECRET_KEY = os.getenv("SECRET_KEY", default=None)


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

if __name__ == "__main__":
    """This runs when you execute '$ python3 s3copy.app'"""
    if ACCESS_KEY is None or SECRET_KEY is None:
        print('Error: environmental variables ACCESS_KEY and SECRET_KEY not defined')
        sys.exit(os.EX_CONFIG)
    elif len(sys.argv)!=3:
        print("Error: expecting exactly two arguments")
        sys.exit(os.EX_CONFIG)
    else:
        uploaded = upload_to_aws(sys.argv[1], 'imgcpy', sys.argv[2])