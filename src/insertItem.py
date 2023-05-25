import boto3
import json
import logging 
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#dynamodbTableName = 'Cities'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Cities')

def handler(event, contest):

    logger.info(event)
    requestBody = json.loads(event['body'])

    try:
        table.put_item(Item = requestBody)
        body = {
            'Operação': 'SALVAR',
            'Mensagem': 'SUCESSO',
            'Item': requestBody
        }

        return buildResponse(200, body)
    
    except:
        logger.exception('Erro ao inserir o novo item!')

def buildResponse(statusCode, body=None):
    response = {
        'statusCode': statusCode,
        'headers': {
            'ContentType': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    if body is not None:
        response['body'] = json.dumps(body)
    return response
