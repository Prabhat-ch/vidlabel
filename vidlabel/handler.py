import boto3
import urllib.parse


def start_label_detection(bucket, keyname):
    rekognition = boto3.client('rekognition')

    response = rekognition.start_label_detection(
        Video={
            'S3Object': {
                'Bucket': bucket,
                'Name': keyname
            }
    })

    print(response)

    return


def process_video(event, context):

    for record in event['Records']:
        start_label_detection(
            record['s3']['bucket']['name'],
            urllib.parse.unquote_plus(record['s3']['object']['key'])
        )

    return
