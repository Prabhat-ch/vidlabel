import os

import json

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
        },
        NotificationChannel={
            'SNSTopicArn': os.environ['REKOGNITION_SNS_TOPIC_ARN'],
            'RoleArn': os.environ['REKOGNITION_ROLE_ARN']
    })

    print(response)

    return

def get_video_labels(job_id):
    rekognition = boto3.client('rekognition')

    response = rekognition.get_label_detection(JobId=job_id)

    next_token = response.get('NextToken', None)

    while next_token:
        next_page = rekognition.get_label_detection(
            JobId=job_id,
            NextToken=next_token
        )

        next_token = next_page.get('NextToken', None)

        response['Labels'].extend(next_page['Labels'])

    return response


def put_labels_in_db(data, s3_object, s3_bucket):
    pass

# Lambda events

def process_video(event, context):

    for record in event['Records']:
        start_label_detection(
            record['s3']['bucket']['name'],
            urllib.parse.unquote_plus(record['s3']['object']['key'])
        )

    return


def handle_label(event, context):

    for record in event['Records']:
        message = json.loads(record['Sns']['Message'])
        job_id = message['JobId']
        s3_object = message['Video']['S3ObjectName']
        s3_bucket = message['Video']['S3Bucket']

        response = get_video_labels(job_id)
        print(response)
        put_labels_in_db(response, s3_object, s3_bucket)

    return
