from fastapi import APIRouter

from services.news_service import NewsService

router = APIRouter()

service = NewsService()


@router.get("/news")

def news():

    return service.latest()