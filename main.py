

from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.router import router

app = FastAPI()

app.include_router(router)

