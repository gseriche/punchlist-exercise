# IaC Testing AWS CDK

This exercise will be to take an existing application and:

- Get the application running in Docker
- Deploy the application to AWS utilizing AWS CDK
- Create a GitHub action workflow to automate the deploy

## How to test the code in Local

To test in local this code you must "export" the variables or use the command `aws configure` to get the keys for AWS.

The account you will use with AWS CDK must have this permissions: 

- cloudformation:DescribeStacks
- cloudformation:CreateChangeSet
- cloudformation:DescribeChangeSet
- cloudformation:ExecuteChangeSet
- cloudformation:DescribeStackEvents
- cloudformation:DeleteChangeSet
- cloudformation:GetTemplate
- arn:aws:cloudformation:${AWS::Region}:${AWS::AccountId}:stack/CDKToolkit/*
- s3:*Object
- s3:ListBucket
- s3:GetBucketLocation

After that you should get the Access Key and secrets to deploy in AWS.

~~~bash
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
export AWS_DEFAULT_REGION=us-west-2
~~~

To install AWS CDK you must have node installed.

~~~bash
npm install -g aws-cdk
~~~

Then you can try the code with

~~~bash
cdk bootstrap
~~~~

After that you can deploy:

~~~bash
cdk deploy
~~~

## How to test the code in GitHub Action

You must create 3 secrets environment variables called:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION

The three first variables must have the same condition explained in the first
paragraph, this variables was used inside the folder
".github/workflows" in the file called "aws-cdk.yml"
