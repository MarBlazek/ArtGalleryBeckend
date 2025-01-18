from database import users_table

def create_user(user_data):
    users_table.put_item(Item=user_data)
    return {"message": "User created successfully"}