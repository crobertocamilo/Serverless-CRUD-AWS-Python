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

        queryStringParameters = event.get('queryStringParameters')
        if queryStringParameters is None:
            #return buildResponse(400, {'Mensagem': 'Parâmetro "Cidade" da solicitação ausente.'})
            return buildResponse(404, {'Mensagem': 'Cidade: %s não encontrada.' % Cidade})
        
        Cidade = event['queryStringParameters']['Cidade']
        
        response = table.get_item(
            Key = {
                'Cidade': Cidade
            }
        )

        if 'Item' in response:
            return buildResponse(200, response['Item'])
        else:
            return buildResponse(404, {f'Mensagem: {Cidade} não encontrada no banco de dados.'})
    
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
