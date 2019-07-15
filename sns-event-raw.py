# coding: utf-8
event = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:us-east-1:382053882751:handle_label_topic:f50d818f-6d17-4ba1-8dfd-9e44b02fb24d', 'Sns': {'Type': 'Notification', 'MessageId': '4330aa20-9017-5ec6-b6c8-ff85d745f9b1', 'TopicArn': 'arn:aws:sns:us-east-1:382053882751:handle_label_topic', 'Subject': None, 'Message': '{"JobId":"d33deed131ae5ad54bcc506b233363c47b603437755eb6c91d25c6321358e53f","Status":"SUCCEEDED","API":"StartLabelDetection","Timestamp":1563116818831,"Video":{"S3ObjectName":"interstellar.mp4","S3Bucket":"vidlabel"}}', 'Timestamp': '2019-07-14T15:06:58.904Z', 'SignatureVersion': '1', 'Signature': 'QVN+aWnMfTv8mvlK2nb+I2GObjG4g219HpzaFOQmv4qd/y7R3uV50j8ZUqrs6Bs25Nwlaxz9RYK07KN/t+fo4YXwyIAbwm5ZoIfg8VGILm3bBEruO8HP88pJCIQor/aEp/4E2q2+C29M7/DHw0qa2cER0Vz/JkOGk+MhOwlGfMDKgS7hhu9RZ1jGzrUjgRHgJLBiCLR9MgdSWqe8z5o6NxkfTZbGTSTs4toQbjFrkxDyUvDr524rG/F1XNKEYbUQFBV5FfogpO9F3WuTcL3DAOKCM7S4MlpH4PsMLok2jOcnjJ1NfwcttLLwf6feeVXB7Q019GzlvyhEVySWBfD/Rg==', 'SigningCertUrl': 'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-6aad65c2f9911b05cd53efda11f913f9.pem', 'UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:382053882751:handle_label_topic:f50d818f-6d17-4ba1-8dfd-9e44b02fb24d', 'MessageAttributes': {}}}]}
event
event['Records']
event['Records'][0]
event.keys()
event['Records'][0].keys()
event['Records'][0]['EventSource']
event['Records'][0]['EventVersion']
event['Records'][0]['EventSubscriptionArn']
event['Records'][0]['Sns']
event['Records'][0]['Sns'].keys()
event['Records'][0]['Sns']['Message']
type(event['Records'][0]['Sns']['Message'])
import jason
import json
json(event['Records'][0]['Sns']['Message'])
json.load(event['Records'][0]['Sns']['Message'])
json.loads(event['Records'][0]['Sns']['Message'])
