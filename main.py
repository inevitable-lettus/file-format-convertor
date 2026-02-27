from fastapi import FastAPI as fapi
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from routers import audio, images, documents, video


@asynccontextmanager
async def lifespan(app: fapi):
    # startup tasks:
    # - ensure temp directory exists
    # - check ffmpeg 
    
    yield

    # shutdown tasks: 
    # - cleanup temp directory

app = fapi (
    titel = "File format converter",
    version = "0.1.0",
    description = "Local file format converter for images, videos, audio and documents. Secure, fast and efficient.",
    lifespan=lifespan,
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=False, 
    allow_methods=["*"],
    allow_headers = ["*"],
)

app.include_router(
    images.router,
    prefix="/convert/image",
    tags=["Images"],
)

app.include_router(
    audio.router,
    prefix="/convert/audio",
    tags=["audio"],
)

app.include_router(
    video.router,
    prefix="/convert/video",
    tags=["video"],
)

app.include_router(
    documents.router,
    prefix="/convert/documents",
    tags=["documents"],
)
