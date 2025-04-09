import boto3

session = boto3.Session(profile_name='test-user')
creds = session.get_credentials().get_frozen_credentials()

print("Access Key:", creds.access_key)
print("Secret Key:", creds.secret_key)
print("Token:", creds.token)

