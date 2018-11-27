import json
import datetime


def handler(event, context):
    print("Received name {}".format(event))
    name = "Andrew"
    if "queryStringParameters" in event:
        if "name" in event["queryStringParameters"]:
            name = event["queryStringParameters"]["name"]
    data = {
        'output': 'Hello ' + name,
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
