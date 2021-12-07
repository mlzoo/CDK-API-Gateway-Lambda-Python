from aws_cdk import (core,
                     aws_apigateway as apigateway,
                     aws_s3 as s3,
                     aws_lambda as lambda_,
                     aws_lambda_python as pylambda_)

class MLService(core.Construct):
    def __init__(self, scope: core.Construct, id: str):
        super().__init__(scope, id)
        
        handler = pylambda_.PythonFunction(self, "MyFunction",
            entry="resources",  # required
            index="lambda_handler.py",  # optional, defaults to 'index.py'
            handler="lambda_handler",  # optional, defaults to 'handler'
            runtime=lambda_.Runtime.PYTHON_3_9
        )
        
        api = apigateway.RestApi(self, "ml-api",
                  rest_api_name="Machine Learning API",
                  description="This service serves ML endpoint")
        
        get_ml_integration = apigateway.LambdaIntegration(handler,
                request_templates={"application/json": '{ "statusCode": "200" }'})

        api.root.add_method("GET", get_ml_integration)   # GET /
        api.root.add_method("POST", get_ml_integration)   # GET /