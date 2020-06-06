from crhelper import CfnResource
import boto3, json

helper = CfnResource()
iamclient = boto3.client('iam')

@helper.create
def create_https_credentials(event, _):
    user = event['ResourceProperties']['user']

    response = iamclient.create_service_specific_credential(
        UserName=user,
        ServiceName='codecommit.amazonaws.com'
    )

    helper.Data['ServiceUserName'] = response['ServiceSpecificCredential']['ServiceUserName']
    helper.Data['ServicePassword'] = response['ServiceSpecificCredential']['ServicePassword']

@helper.update
def reset_https_credentials(event, _):
    user = event['ResourceProperties']['user']
    
    response = iamclient.reset_service_specific_credential(
        UserName=user,
        ServiceName='codecommit.amazonaws.com'
    )

    helper.Data['ServiceUserName'] = response['ServiceSpecificCredential']['ServiceUserName']
    helper.Data['ServicePassword'] = response['ServiceSpecificCredential']['ServicePassword']

@helper.delete
def delete_https_credentials(event, _):
    user = event['ResourceProperties']['user']

    iamclient.delete_service_specific_credential(
        UserName=user,
        ServiceName='codecommit.amazonaws.com'
    )

def handler(event, context):
    print("Started execution of HTTPS Credentials Creator Lambda...")
    print("Function ARN %s" % context.invoked_function_arn)
    print("Incoming Event %s " % json.dumps(event))
    
    helper(event, context)