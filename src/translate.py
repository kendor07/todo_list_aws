import json
import decimalencoder
import todoList
import boto3


def translate(event, context):
    # create a response
    item = todoList.get_item(event['pathParameters']['id'])
    lang = event['pathParameters']['id']['lang']
    if item:
        translate = boto3.client(service_name='translate',
                                 region_name='us-east-1',
                                 use_ssl=True)
        result = translate.translate_text(Text=item.text,
                                          SourceLanguageCode="en",
                                          TargetLanguageCode=lang)
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
