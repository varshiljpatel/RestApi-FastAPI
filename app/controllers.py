from pymongo.errors import DuplicateKeyError
from app.collections import collection
from app.models import User

# Create a new user
async def create_user(user : User):
    try:
        insert_user = collection.insert_one(user.dict())
        user_id = str(insert_user.insertrd_id)
        return {
            "id" : user_id,
            "message" : "User inserted successfully"
        }
    except DuplicateKeyError:
        raise ValueError("User already exists")

# Get all Users
async def get_users():
    get_all_users = collection.find()
    return [user for user in get_all_users]

# Geta single user
async def get_user(user_id : str):
    get_single_user = collection.find_one({"_id": user_id})
    if get_single_user :
        return get_single_user 
    else:
        raise ValueError("User not found")

# Update an user
async def update_user(user_id : str, user : User):
    update_user_details = collection.update_one({
        "_id": user_id,
    }, {
        "$set" : user.dict()
    })
    if update_user_details.modified_count == 1 :
        return {"message": "User updated successfully"}
    else:
        raise ValueError("User not found")

# Delete a user
async def delete_user(user_id: str):
    delete_user_from_database = collection.delete_one({
        "_id": user_id,
    })
    if delete_user_from_database.deleted_count == 1 :
        return {"message": "User deleted successfully"}
    else:
        raise ValueError("User not found")