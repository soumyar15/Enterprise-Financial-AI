from fastapi import APIRouter

from services.document_service import DocumentService

router = APIRouter()

service = DocumentService()


@router.post("/upload")

def upload():

    return service.upload()