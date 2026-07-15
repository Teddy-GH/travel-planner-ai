from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router



app = FastAPI(
    title="Travel Planner AI"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
async def root():
    return {
        "message": "Backend Running"
    }