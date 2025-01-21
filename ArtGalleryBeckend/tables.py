import boto3
from botocore.exceptions import NoCredentialsError

# Povezivanje na lokalni DynamoDB
dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url='http://localhost:8000',  # Lokalni DynamoDB
    region_name='us-west-2',  # Možeš postaviti bilo koji region
)

# Funkcija za kreiranje tablice 'users'
def create_users_table():
    try:
        table = dynamodb.create_table(
            TableName='users',
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'  # Primarni ključ
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'  # String tip
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        print("Table created successfully")
    except Exception as e:
        print(f"Error creating table: {e}")

# Ovdje pozivaš funkciju
create_users_table()