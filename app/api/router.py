from fastapi import APIRouter

from app.api.endpoints import model

router = APIRouter()
router.include_router(model.router)
