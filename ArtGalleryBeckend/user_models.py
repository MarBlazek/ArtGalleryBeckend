from pydantic import BaseModel
from typing import Optional
from tables import dynamodb

# Povezivanje na tablicu 'users' s pomoću DynamoDB resursa
users_table = dynamodb.Table('users')
galleries_table = dynamodb.Table('galleries')
artworks_table = dynamodb.Table('artworks')

# Definicija Pydantic modela
class User(BaseModel):
    id: str
    name: str
    email: str
    date_registered: str

class Gallery(BaseModel):
    id: str
    title: str
    description: Optional[str] = None

class Artwork(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    artist_id: str

# CRUD operacije za korisnike
def create_user(user_data):
    """
    Kreira novog korisnika u tablici 'users'.
    """
    try:
        users_table.put_item(Item=user_data)
        return {"message": "User created successfully"}
    except Exception as e:
        return {"error": str(e)}

def get_user(user_id):
    """
    Dohvaća korisnika prema njegovom ID-u iz tablice 'users'.
    """
    response = users_table.get_item(Key={'id': user_id})
    item = response.get('Item')
    if item:
        return item
    else:
        return {"message": "User not found"}

def update_user(user_id, updated_data):
    """
    Ažurira podatke korisnika prema njegovom ID-u u tablici 'users'.
    """
    response = users_table.update_item(
        Key={'id': user_id},
        UpdateExpression="set name=:n, email=:e, date_registered=:d",
        ExpressionAttributeValues={
            ':n': updated_data['name'],
            ':e': updated_data['email'],
            ':d': updated_data['date_registered']
        },
        ReturnValues="UPDATED_NEW"
    )
    return {"message": "User updated successfully", "updated_attributes": response['Attributes']}

def delete_user(user_id):
    """
    Briše korisnika prema njegovom ID-u iz tablice 'users'.
    """
    users_table.delete_item(Key={'id': user_id})
    return {"message": "User deleted successfully"}