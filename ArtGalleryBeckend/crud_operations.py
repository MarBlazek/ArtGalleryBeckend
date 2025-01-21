from database import users_table, galleries_table, artworks_table


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
    try:
        response = users_table.get_item(Key={'id': user_id})
        item = response.get('Item')
        if item:
            return item
        else:
            return {"message": "User not found"}
    except Exception as e:
        return {"error": str(e)}


def update_user(user_id, updated_data):
    """
    Ažurira podatke korisnika prema njegovom ID-u u tablici 'users'.
    """
    try:
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
    except Exception as e:
        return {"error": str(e)}


def delete_user(user_id):
    """
    Briše korisnika prema njegovom ID-u iz tablice 'users'.
    """
    try:
        users_table.delete_item(Key={'id': user_id})
        return {"message": "User deleted successfully"}
    except Exception as e:
        return {"error": str(e)}


# CRUD operacije za galerije
def create_gallery(gallery_data):
    """
    Kreira novu galeriju u tablici 'galleries'.
    """
    try:
        galleries_table.put_item(Item=gallery_data)
        return {"message": "Gallery created successfully"}
    except Exception as e:
        return {"error": str(e)}


def get_gallery(gallery_id):
    """
    Dohvaća galeriju prema njenom ID-u iz tablice 'galleries'.
    """
    try:
        response = galleries_table.get_item(Key={'id': gallery_id})
        item = response.get('Item')
        if item:
            return item
        else:
            return {"message": "Gallery not found"}
    except Exception as e:
        return {"error": str(e)}


def update_gallery(gallery_id, updated_data):
    """
    Ažurira podatke galerije prema njenom ID-u u tablici 'galleries'.
    """
    try:
        response = galleries_table.update_item(
            Key={'id': gallery_id},
            UpdateExpression="set title=:t, description=:d",
            ExpressionAttributeValues={
                ':t': updated_data['title'],
                ':d': updated_data['description']
            },
            ReturnValues="UPDATED_NEW"
        )
        return {"message": "Gallery updated successfully", "updated_attributes": response['Attributes']}
    except Exception as e:
        return {"error": str(e)}


def delete_gallery(gallery_id):
    """
    Briše galeriju prema njenom ID-u iz tablice 'galleries'.
    """
    try:
        galleries_table.delete_item(Key={'id': gallery_id})
        return {"message": "Gallery deleted successfully"}
    except Exception as e:
        return {"error": str(e)}


# CRUD operacije za umjetnička djela
def create_artwork(artwork_data):
    """
    Kreira novo umjetničko djelo u tablici 'artworks'.
    """
    try:
        artworks_table.put_item(Item=artwork_data)
        return {"message": "Artwork created successfully"}
    except Exception as e:
        return {"error": str(e)}


def get_artwork(artwork_id):
    """
    Dohvaća umjetničko djelo prema njegovom ID-u iz tablice 'artworks'.
    """
    try:
        response = artworks_table.get_item(Key={'id': artwork_id})
        item = response.get('Item')
        if item:
            return item
        else:
            return {"message": "Artwork not found"}
    except Exception as e:
        return {"error": str(e)}


def update_artwork(artwork_id, updated_data):
    """
    Ažurira podatke umjetničkog djela prema njegovom ID-u u tablici 'artworks'.
    """
    try:
        response = artworks_table.update_item(
            Key={'id': artwork_id},
            UpdateExpression="set title=:t, description=:d, artist_id=:a",
            ExpressionAttributeValues={
                ':t': updated_data['title'],
                ':d': updated_data['description'],
                ':a': updated_data['artist_id']
            },
            ReturnValues="UPDATED_NEW"
        )
        return {"message": "Artwork updated successfully", "updated_attributes": response['Attributes']}
    except Exception as e:
        return {"error": str(e)}


def delete_artwork(artwork_id):
    """
    Briše umjetničko djelo prema njegovom ID-u iz tablice 'artworks'.
    """
    try:
        artworks_table.delete_item(Key={'id': artwork_id})
        return {"message": "Artwork deleted successfully"}
    except Exception as e:
        return {"error": str(e)}

"""
create_user() - Dodaje korisnika u tablicu users.

get_user() - Dohvaća korisnika prema ID-u iz tablice users.

update_user() - Ažurira korisničke podatke u tablici users.

delete_user() - Briše korisnika iz tablice users.

create_gallery() - Dodaje novu galeriju u tablicu galleries.

get_gallery() - Dohvaća galeriju prema ID-u iz tablice galleries.

update_gallery() - Ažurira galeriju u tablici galleries.

delete_gallery() - Briše galeriju iz tablice galleries.

create_artwork() - Dodaje novo umjetničko djelo u tablicu artworks.

get_artwork() - Dohvaća umjetničko djelo prema ID-u iz tablice artworks.

update_artwork() - Ažurira umjetničko djelo u tablici artworks.

delete_artwork() - Briše umjetničko djelo iz tablice artworks.
"""