# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='videolyzer')
from pathlib import Path
get_ipython().run_line_magic('ls', '~/')
pathname = "~/Dog grass-YVdkW0f_6sQ.mp4"
path = Path(pathname)
path = Path(pathname).expanduser().resolve()
response = bucket.upload_file(str(path), str(path.name))
rekognition = session.client('rekognition')

response = rekognition.start_label_detection(
Video={
'S3Object': {
'Bucket': str(bucket.name),
'Name': str(path.name)}
})

labels = rekognition.get_label_detection(JobId=response['JobId'])
