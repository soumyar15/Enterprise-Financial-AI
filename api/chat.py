from fastapi import APIRouter

from models.request_models import QueryRequest

from services.query_service import QueryService

router = APIRouter()

service = QueryService()


@router.post("/chat")

def chat(request: QueryRequest):

    return service.process(request.question)