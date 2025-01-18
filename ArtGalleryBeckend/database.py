import boto3

# Stvaranje klijenta za DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Definicija tablica
users_table = dynamodb.Table('users')
galleries_table = dynamodb.Table('galleries')
artworks_table = dynamodb.Table('artworks')