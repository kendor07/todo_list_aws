import json
import decimalencoder
import todoList
import boto3


def translate(event, context):
    # create a response
    item = todoList.get_item(event['pathParameters']['id'])
    lang = event['pathParameters']['lang']
    if item and lang:
        result = todoList.translate_items(item["text"], lang)
        response = {
            "statusCode": 200,
            "body": json.dumps(result,
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response
