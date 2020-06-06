# codecommit-httpscreds-cloudformation

To use:
1. Setup AWS CLI for the user and region desired. Ensure IAM user has sufficient IAM privilages to deploy the resources
2. Create the 00_shared-infrastructure.yaml CFN stack. This stack creates the S3 Bucket used for the Lambda package to be deployed in the next stack
3. Deploy the lambda package httpscreds to the S3 bucket created in step 2.
4. Create the 10_credentials-creator-lambda.yaml CFN stack. This deploys the Lambda to the bucket created in the previous stack
5. Create the 20_create-codecommit-user.yaml CFN stack. This creates an IAM User for the provided 'username' parameter, creates an IAM Group (admin) with administrator access adds the user to the group. The stack then creates the custom https credentials resource, and presents the IAM User Keys, and the HTTPS Credentials to the outputs section of the stack.

Note: 20_create-codecommit-user.yaml creates the admin IAM group. This will cause subsequent deployments of the stack to fail. To fix this, the IAM group resource declaration needs to be moved to the shared infrastructure stack, and the reference to the group will need to be an exported output, imported by the user stack.

