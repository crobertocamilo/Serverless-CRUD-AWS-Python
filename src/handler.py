import json


def status(event, context):
    body = {
        "message": "A API está online!"
        #"input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
