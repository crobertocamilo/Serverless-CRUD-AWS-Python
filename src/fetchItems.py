import boto3
import json
import logging 
logger = logging.getLogger()
logger.setLevel(logging.INFO)
import decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Cities')

def handler(event, context):

    logger.info(event)

    try:

        response = table.scan()
        result = response['Items']

        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey = response['LastEvaluatedKey'])
            result.extend(response['Items'])

        body = {
            'Cidade': result

        }

        return buildResponse(200, body)
    
    except:
        logger.exception('Erro ao realizar a pesquisa!')

def buildResponse(statusCode, body=None):
    response = {
        'statusCode': statusCode,
        'headers': {
            'ContentType': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    if body is not None:
        response['body'] = json.dumps(body, default=decimal_default)
    
    return response

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError
