from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Video Translator")
app.include_router(router)