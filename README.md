# IaC Testing AWS CDK

This exercise will be to take an existing application and:

- Get the application running in Docker
- Deploy the application to AWS utilizing AWS CDK
- Create a GitHub action workflow to automate the deploy

## How to test the code in Local

To test in local this code you must "export" the 

~~~bash
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
export AWS_DEFAULT_REGION=us-west-2
~~~


## How to test the code in GitHub Action

You must create 3 secrets environment variables called:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION

The three first variables must have the same condition explained in the first
paragraph, after that you should create a SSH_KEY variable having your private
key and get access to the repository, this variables was used inside the folder
".github/workflows" in the file called "terratest-action.yml"
