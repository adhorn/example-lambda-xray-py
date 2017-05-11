# What's up?
Example Lambda Function running Python and X-ray using the https://github.com/racker/fleece/ 

# Build dependencie package
1. Run the following commands:
```
mkdir .vendor
pip install -r requirements.txt -t .vendor
serverless deploy
```
2. Got to the AWS Lambda Console and enable active tracing for the function.

3. Make sure your lambda function has permission to access GetUser in IAM and use X-Ray by creating a role with the following policy.
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "logs:CreateLogStream"
                "xray:PutTraceSegments",
                "xray:PutTelemetryRecords",
                "logs:PutLogEvents"
                "iam:Get*"
            ],
            "Resource": [
                "*"
            ],
            "Effect": "Allow"
        }
    ]
}
```

4. Invoke your function and text X-Ray with Python
```
serverless invoke -f hello -l
```
