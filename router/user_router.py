from fastapi import APIRouter, HTTPException
from app.models import User
from app.controllers import (
    create_user,
    get_users,
    get_user,
    update_user,
    delete_user
)

# Create a router isinstance
router = APIRouter()

@router.post('/user')
async def create_user_route(user: User):
    try:
        return await create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get('/users')
async def get_users_route():
    return await get_users()

@router.get('/user/{user_id}')
async def get_user_route(user_id: str):
    try:
        return await get_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put('/user/{user_id}')
async def update_user_route(user_id: str, user: User):
    try:
        return await update_user(user_id, user)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete('/user/{user_id}')
async def delete_user_route(user_id: str):
    try:
        return await delete_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))