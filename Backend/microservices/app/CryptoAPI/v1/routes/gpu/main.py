from fastapi import APIRouter

router = APIRouter()


@router.get('/test')
async def root():
    pass