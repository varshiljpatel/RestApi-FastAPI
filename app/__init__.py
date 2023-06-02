from fastapi import FastAPI
from router.user_router import router

# Create an instance
app = FastAPI()

app.include_router(router)