aws iam create-role --role-name lambda-ex --assume-role-policy-document file://trust-policy.json


aws lambda create-function --function-name my-function --zip-file fileb://function.zip --handler lambda_function.lambda_handler --runtime python3.8 --role arn:aws:iam::091455609400:role/lambda-ex
