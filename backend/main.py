from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Choose your own aAdventure game API",
    description="Api to generate cool stories",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)