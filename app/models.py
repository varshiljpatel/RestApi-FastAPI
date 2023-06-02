from pydantic import BaseModel

# Create an user model
class User(BaseModel):
    name: str
    email: str