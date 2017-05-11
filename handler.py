import sys
sys.path.insert(0, './.vendor')

from datetime import datetime
from json import dumps
from fleece import boto3
from fleece.xray import (monkey_patch_botocore_for_xray)

monkey_patch_botocore_for_xray()


# @trace_xray_subsegment
def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": get_user()
    }

    response = {
        "statusCode": 200,
        "body": body
    }

    return response


def get_user():
    # This function doesn't have to be decorated, because the API call to IAM
    # will be traced thanks to the monkey-patching.
    iam = boto3.client('iam')
    return dumps(iam.get_user(UserName="aws_cli"), default=json_serial)


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError ("Type not serializable")