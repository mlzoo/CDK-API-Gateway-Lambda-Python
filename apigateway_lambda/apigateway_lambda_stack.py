from aws_cdk import (
    core as cdk
    # aws_sqs as sqs,
)
from . import ml_service


from aws_cdk import core


class ApigatewayLambdaStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ml_service.MLService(self, "ml")
        
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "ApigatewayLambdaQueue",
        #     visibility_timeout=cdk.Duration.seconds(300),
        # )
