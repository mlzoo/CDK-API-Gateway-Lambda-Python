import os
import json
import sagemaker
        
def lambda_handler(event, context):
    json_region = os.environ['AWS_REGION']
    # get = event['queryStringParameters']
    post = event['body']
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Region ": json_region,
            "ret" : post,
            "sagemaker" : str(sagemaker)
            
        })
    }