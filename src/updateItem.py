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

    requestBody = json.loads(event['body'])

    Cidade = requestBody['Cidade']
    updateKey = requestBody['updateKey']
    updateValue = requestBody['updateValue']

    try:

        response = table.update_item(
            Key = {
                'Cidade': Cidade
            },
            UpdateExpression='set %s = :value' % updateKey,
            ExpressionAttributeValues={
                ':value': updateValue
            },
            ReturnValues='UPDATED_NEW'
        )

        body = {
            'Operação': 'SALVAR',
            'Mensagem': 'SUCESSO',
            'Item': requestBody
        } 

        return buildResponse(200, body)       
    
    except:
        logger.exception('Erro ao realizar a alteração!')

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
