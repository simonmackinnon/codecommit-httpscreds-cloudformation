# codecommit-httpscreds-cloudformation

To use:
1. Setup AWS CLI for the user and region desired. Ensure IAM user has sufficient IAM privilages to deploy the resources
2. Create the 00_shared-infrastructure.yaml CFN stack. This stack creates the S3 Bucket used for the Lambda package to be deployed in the next stack

e.g.
aws cloudformation create-stack --stack-name Shared-Infrastructure --template-body file://00_shared-infrastructure.yaml --parameters ParameterKey=groupname,ParameterValue=codecommitters --capabilities CAPABILITY_NAMED_IAM

3. Deploy the lambda package httpscreds to the S3 bucket created in step 2.

e.g.
aws s3 cp ./httpscreds.zip s3://shared-infrastructure-s3lambdabucket-1sh3dfvghas3q

4. Create the 10_credentials-creator-lambda.yaml CFN stack. This deploys the Lambda to the bucket created in the previous stack

e.g.
aws cloudformation create-stack --stack-name CredentialsCreator --template-body file://10_credentials-creator-lambda.yaml --capabilities CAPABILITY_NAMED_IAM

5. Create the 20_create-codecommit-user.yaml CFN stack. This creates an IAM User for the provided 'username' parameter, creates an IAM Group (admin) with administrator access adds the user to the group. The stack then creates the custom https credentials resource, and presents the IAM User Keys, and the HTTPS Credentials to the outputs section of the stack.

e.g.
aws cloudformation create-stack --stack-name CodeCommitUser --template-body file://20_create-codecommit-user.yaml  --parameters ParameterKey=username,ParameterValue=codecommituser --capabilities CAPABILITY_NAMED_IAM

